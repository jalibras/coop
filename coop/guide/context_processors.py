

from guide.models import Area

def nav(request):
    areas = Area.objects.all()
    return {
            'areas':areas,
    }

