from django.shortcuts import render
from django.forms import inlineformset_factory, ValidationError
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

from guide.models import BaseProblem,NaturalProblem,Area,ProblemImage,ProblemVideo,Comment
from guide.forms import ProblemVideoForm,CommentForm,NaturalProblemForm,AddNaturalProblemForm

# Create your views here.


#def navigatio


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
    prob_list = BaseProblem.objects.filter(area=area)
    arlist = Area.objects.all()
    return render(request,'guide/area.html',{
        'area':area,
        'arlist':arlist,
        'prob_list':prob_list,
        })


@login_required
def submitproblem(request,**kwargs):

    problemimage_formset=inlineformset_factory(NaturalProblem,ProblemImage,fields=['image_file'],extra=1)
    if request.method=='POST':
        # process form submission
        if request.POST['problem_type']=='natural':
            form = AddNaturalProblemForm(request.POST)
            formset = problemimage_formset(request.POST)
            if form.is_valid() and formset.is_valid():
                prob = form.save(commit=False)
                images  = formset.save(commit=False)
                for image in images:
                    image.problems = prob
                    image.save(commit=False)
                if prob.problemimage_set.all().count()==0 and len(images)==0:
                    raise ValidationError('You must have at least one image')
                else:
                    prob.save()
                    for image in images:
                        image.save()

                return HttpResponse('Problem saved')
            #else:
            #    return HttpResponse('Problem not saved')
        else:
            return HttpResponse('unknown problem type')
        pass
    else:
        if request.GET.get('type')=='natural':
            form = AddNaturalProblemForm()
            formset = problemimage_formset()
        else:
            return HttpResponse('unknown problem type')

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



