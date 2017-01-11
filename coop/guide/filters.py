import django_filters

from guide.models import ArtificialProblem

class ArtificialProblemFilter(django_filters.FilterSet):
    class Meta:
        model = ArtificialProblem
        fields={
                'sector':['exact'],
                'grade':['exact'],
                }

    @property
    def qs(self):
        parent = super(ArtificialProblemFilter,self).qs
