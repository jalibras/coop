from django.shortcuts import render

from django.http import Http404

from guide.models import BaseProblem,Area

# Create your views here.


#def navigatio


def index(request):
    """
    view for homepage
    """
    area_id=int(request.GET.get('areaid',default=1))
    area = Area.objects.get(id=area_id)
    prob_list = BaseProblem.objects.filter(area=area)
    return render(request,'guide/index.html',{
        'area':area,
        'prob_list':prob_list,
        })


def problem(request,id):
    """
    view a problem
    """
    subcls_list = BaseProblem.__subclasses__()
    for cls in subcls_list:
        try:
            problem = cls.objects.get(id=int(id))
            break
        except:
            pass
    else:
        raise Http404

    return render(request,'guide/problem.html',{
        'request':request,
        'problem':problem,
        })



