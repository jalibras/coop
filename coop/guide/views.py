from django.shortcuts import render

from django.http import Http404

from guide.models import Problem

# Create your views here.


#def navigatio


def index(request):
    """
    view for homepage
    """
    prob_list = Problem.objects.all()
    return render(request,'guide/index.html',{
        'prob_list':prob_list,
        })


def problem(request,id):
    """
    view a problem
    """
    try:
        problem = Problem.objects.get(id = int(id))
    except:
        raise Http404

    return render(request,'guide/problem.html',{
        'request':request,
        'problem':problem,
        })



