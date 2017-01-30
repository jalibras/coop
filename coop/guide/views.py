from django.shortcuts import render
from django.forms import inlineformset_factory, ValidationError
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.core.mail import send_mail
from django.utils.html import mark_safe,format_html
from django.utils import timezone


from rest_framework import viewsets
#from rest_framework.filters import SearchFilter

from guide.models import BaseProblem,ArtificialProblem,NaturalProblem,Area,Sector,ProblemImage,ProblemVideo,Comment,ProblemByMember
from guide.forms import ProblemVideoForm,CommentForm,AddArtificialProblemForm,AddNaturalProblemForm,ProblemByMemberForm,ProblemImageInlineForm,ProblemFlagForm
from guide.serializers import ArtificialProblemSerializer, NaturalProblemSerializer, ProblemImageSerializer, AreaSerializer, SectorSerializer



from members.decorators import member_required
from members.models import User

# import for class based views

from django.views.generic import ListView


# Create your views here.


# placeholder for permissions method
def permission(*args,**kwargs):
# we need to implement permission logic 
    return True



class ArtificialProblemList(ListView):
    model = ArtificialProblem


    def get_queryset(self,*args,**kwargs):
        qs = super(ArtificialProblemList,self).get_queryset(*args,**kwargs)
        if 'sector__id' in self.request.GET:
            qs = qs.filter(sector__id=self.request.GET.get('sector__id'))
        if 'area__id' in self.request.GET:
            qs = qs.filter(area__id=self.request.GET.get('area__id'))

        return qs

    #def get_context_data(self,**kwargs):
    #    context = super(ArtificialAreaView,self).get_context_data(**kwargs)




def index(request):
    """
    view for homepage
    """
    arlist = Area.objects.all()
    return render(request,'guide/index.html',{
        'arlist':arlist,
        })

def area(request,areaid=1):
    """
    view for homepage
    """
    area = Area.objects.get(id=areaid)
    ord_by = request.GET.get('order_by','grade')
    prob_list = BaseProblem.objects.filter(area=area).order_by(ord_by)
    arlist = Area.objects.all()
    if hasattr(request.user,'member'):
        member_context = {
                'done':{p:p.problembymember_set.filter(member=request.user.member).count()!=0 for p in prob_list},
                }
    else:
        member_context=None
    return render(request,'guide/area.html',{
        'area':area,
        'arlist':arlist,
        'prob_list':prob_list,
        'ob':ord_by,
        })


def sector(request,sectorid=1):
    """
    view for homepage
    """
    sector = Sector.objects.get(id=sectorid)
    ord_by = request.GET.get('order_by','grade')
    prob_list = BaseProblem.objects.filter(sector=sector,approved=True,exists=True).order_by(ord_by)
    arlist = Area.objects.all()
    if hasattr(request.user,'member'):
        member_context = {
                'done':{p:p.problembymember_set.filter(member=request.user.member).count()!=0 for p in prob_list},
                }
    else:
        member_context=None
    return render(request,'guide/sector.html',{
        'area':sector.area,
        'sector':sector,
        'arlist':arlist,
        'prob_list':prob_list,
        'ob':ord_by,
        })


def area_map(request,area_id):
    recent_comments = Comment.objects.filter(problem__area=area_id,created__gte=timezone.now()-timezone.timedelta(days=7))
    recently_discussed = set([c.problem for c in recent_comments])
    area = Area.objects.get(id = area_id)
    return render(request,'guide/clickable_area_map.html',{
        'recently_discussed':recently_discussed,
        'area':area,
        })


#def clickable_area_map(request,area_id):
#    area = Area.objects.get(id = area_id)
#    return render(request,'guide/clickable_area_map.html',{
#        'area':area,
#        })

@user_passes_test(lambda u:hasattr(u,'member'))
def submitproblem(request,**kwargs):

# if kwargs has problem_id then we are updating existing and we 
# infer the problem_type from that. If it does not have 
# problem_id then it must have problem_type 

    if 'problem_id' in kwargs: # then we are updating an existing
        base_instance = BaseProblem.objects.get(id=kwargs.pop('problem_id'))
        if request.user.member != base_instance.owner and base_instance.owner.id != 117:
            return HttpResponse("you can't mess around like that! You have to be the owner of the problem to edit it. I'm watching you {fn}...".format(fn=request.user.first_name))
        if hasattr(base_instance,'artificialproblem'):
            instance = base_instance.artificialproblem
            problem_type='artificial'
        elif hasattr(base_instance,'naturalproblem'):
            instance = base_instance.naturalproblem
            problem_type='natural'
    else: # then we must have a problem_type kwarg
        instance = None
        problem_type = kwargs.pop('problem_type')
        print(problem_type)

            


    ProblemImageFormSet=inlineformset_factory(BaseProblem,ProblemImage,form=ProblemImageInlineForm, fields=['image_file'],extra=2,can_delete=True)
    if request.method=='POST':
        # prepolulate the form with defaults
        kws = { 'initial':{ k:request.GET.get(k) for k in request.GET}, }
        if problem_type=='natural':

            form = AddNaturalProblemForm(request.POST,request.FILES,instance=instance,**kws)
        elif problem_type=='artificial':
            form = AddArtificialProblemForm(request.POST,request.FILES,instance=instance,**kws)
        else:
            return HttpResponse('unknown problem type')

        formset = ProblemImageFormSet(request.POST,request.FILES,instance=instance)
        if form.is_valid():

            prob = form.save()
            prob.owner=request.user.member
            prob.save(force_update=True)

            formset.instance=prob
            if formset.is_valid():
                    formset.save()

                # now check to see if the problem has any images and update the image required flag - TODO (maybe not?)
            return render(request,'guide/message.html',{
                'message':"Your problem has been saved",
                'next':reverse('guide:problem',args=[prob.id]),
                })

    else:
        # prepolulate the form with defaults
        kws = { 'initial':{ k:request.GET.get(k) for k in request.GET}, }
        if request.GET.get('area'):
            kws['area_id']=request.GET.get('area')
        if problem_type=='natural':
            form = AddNaturalProblemForm(instance=instance,**kws)
        elif problem_type=='artificial':
            form = AddArtificialProblemForm(instance=instance,**kws)
        else:
            return HttpResponse('unknown problem type')
        formset = ProblemImageFormSet(instance=instance)

    return render(request,'guide/problem_submission.html',{
                'instance':instance,
                'problem_type':problem_type,
                'form':form,
                'fs':formset,
                })


def problem(request,id):
    """
    view a problem
    """
    
    try:
        problem = BaseProblem.objects.get(id = int(id))
    except:
        raise Http404

    if request.method =='POST':
        if request.POST['post-type']=='video':
            form = ProblemVideoForm(request.POST)
            if form.is_valid():
                vid = ProblemVideo(embed_code=form.cleaned_data['embed_code'],problem=problem)
                try:
                    vid.member=request.user.member_set.all()[0]
                except:
                    pass
    
                vid.save()
                return HttpResponseRedirect(request.path)
                #return HttpResponse('Video link saved with id = {id}'.format(id=vid.id))
            else:
                raise ValueError
        
        elif request.POST['post-type']=='comment':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(text=form.cleaned_data['text'],problem=problem)
                try:
                    comment.member=request.user.member
                except:
                    pass

                
                comment.save()
                
                if problem.owner.notifications:
                    try:
                        message = format_html(mark_safe(""" Hi {ownerfn}, \n{fn} {ln} has posted a comment on a problem that you submitted to the co-op database. \n \n See all comments on this problem at http://galwayclimbing.pythonanywhere.com{url} """),
                                ownerfn=problem.owner.user.first_name, 
                                fn=request.user.first_name, 
                                ln=request.user.last_name, 
                                url=reverse('guide:problem',args=[problem.id])
                            )
                        to = problem.owner.user.email
                        subject='Someone posted a comment on one of your problems at the coop'
                        send_mail(
                                subject,
                                message,
                                'galwayclimberscoop@gmail.com',
                                [to]
                                )
                    except:
                        pass


                return HttpResponseRedirect(request.path)
                #return HttpResponse('Video link saved with id = {id}'.format(id=vid.id))
            else:
                raise ValueError

    videoform=ProblemVideoForm()
    commentform=CommentForm()

    return render(request,'guide/problem.html',{
        'request':request,
        'problem':problem,
        'videoform':videoform,
        'commentform':commentform,
        })



@user_passes_test(lambda u:hasattr(u,'member'))
def problem_flag(request,problem_id):
    if request.method=='POST':
        form = ProblemFlagForm(request.POST)
        if form.is_valid():
            problem = BaseProblem.objects.get(id=problem_id)
            flag = form.save(commit=False)
            flag.problem = problem
            flag.member=request.user.member
            flag.save()
            return render(request,'guide/problem_flag.html',{
                'problem':problem,
                'problem_id':problem_id,
                'submission_accepted':True,
                })
    else:
        form = ProblemFlagForm()
        return render(request,'guide/problem_flag.html',{
            'problem_id':problem_id,
            'submission_accepted':False,
            'form':form,
            })


# views to handle AJAX requests

def toggle_problem_status(request,userid,problemid):
    try:
        m = User.objects.get(id=userid).member
        p = BaseProblem.objects.get(id=problemid)
    except:
        raise ValueError('something is wrong')

    if m in p.done_by.all():
        p.done_by.remove(m)
    else:
        p.done_by.add(m)

    return HttpResponse('OK')

def get_problem_status(request,userid,problemid):
    m = User.objects.get(id = userid).member
    p = BaseProblem.objects.get(id=problemid)
    if m in p.done_by.all():
        return HttpResponse('<span class="glyphicon glyphicon-ok problem-member-done"></span>')
    else:
        return HttpResponse('<span class="glyphicon glyphicon-remove problem-member-notdone"></span>')





# Django REST views
class NaturalProblemViewSet(viewsets.ModelViewSet):
    queryset = NaturalProblem.objects.all()
    serializer_class = NaturalProblemSerializer

class ArtificialProblemViewSet(viewsets.ModelViewSet):
    queryset = ArtificialProblem.objects.all()
    serializer_class = ArtificialProblemSerializer
    filter_fields=(
            'grade',
            'setter',
            'sector',
            'area',
            'owner',
            'approved',
            'exists',
            )
    search_fields=(
            'setter',
            'description',
            )
 
class ProblemImageViewSet(viewsets.ModelViewSet):
    queryset = ProblemImage.objects.all()
    serializer_class = ProblemImageSerializer

 
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

 
class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


