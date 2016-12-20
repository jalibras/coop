from django.shortcuts import render
from django.forms import inlineformset_factory, ValidationError
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse

from guide.models import BaseProblem,NaturalProblem,Area,ProblemImage,ProblemVideo,Comment
from guide.forms import ProblemVideoForm,CommentForm,AddArtificialProblemForm,AddNaturalProblemForm

from members.decorators import member_required

# Create your views here.


# placeholder for permissions method
def permission(*args,**kwargs):
# we need to implement permission logic 
    return True



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
    prob_list = BaseProblem.objects.filter(area=area,approved=True).order_by(ord_by)
    arlist = Area.objects.all()
    return render(request,'guide/area.html',{
        'area':area,
        'arlist':arlist,
        'prob_list':prob_list,
        })


@user_passes_test(lambda u:hasattr(u,'member'))
def submitproblem(request,**kwargs):

    ProblemImageFormSet=inlineformset_factory(NaturalProblem,ProblemImage,fields=['image_file'],extra=2)
    if request.method=='POST':
        # process form submission - need to add validation and to ensure that each problem has at least one image. Maybe do this with an extra field in the BaseProblem model for image required that defaults to True. Problem is only published when image required is False. 
        if request.GET.get('type')=='natural':

            form = AddNaturalProblemForm(request.POST,request.FILES)
        elif request.GET.get('type')=='artificial':
            form = AddArtificialProblemForm(request.POST,request.FILES)
        else:
            return HttpResponse('unknown problem type')

        formset = ProblemImageFormSet(request.POST,request.FILES)
        if form.is_valid():
            prob = form.save()
            prob.owner=request.user.member
            prob.save(force_update=True)
            # now stop anyone trying to add a different owner
            if prob.owner !=request.user.member:
                raise ValueError('Woah!')

            formset.instance=prob
            if formset.is_valid():
                    formset.save()

                # now check to see if the problem has any images and update the image required flag - TODO
            return render(request,'guide/message.html',{
                'message':"Your problem has been saved",
                'next':reverse('guide:area',args=[prob.area.id]),
                })
        #HttpResponse('Problem saved')

    else:
        if request.GET.get('type')=='natural':
            # prepopulates the form with get values from the request
            form = AddNaturalProblemForm(initial={ k:request.GET.get(k) for k in request.GET} )
        elif request.GET.get('type')=='artificial':
            form = AddArtificialProblemForm(initial={ k:request.GET.get(k) for k in request.GET} )
        else:
            return HttpResponse('unknown problem type')
        formset = ProblemImageFormSet()

    return render(request,'guide/problem_submission.html',{
                'problem_type':'natural',
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



