from django.shortcuts import render

from django.http import Http404

# Create your views here.


#def navigatio


def index(request):
    """
    view for homepage
    """
    return render(request,'guide/index.html',{
        'maincontent':'Placeholder for the problem guide',
        })


def problem(request,id):
    """
    view a problem
    """
    try:
        problem = Problem.objects.get(id = id)
    except:
        raise Http404

    return render(request,'guide/problem.html',{
        'request':request,
        'problem':problem,
        })



