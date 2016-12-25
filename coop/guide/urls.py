from django.conf.urls import url

from guide import views

from guide.views import ArtificialProblemList



urlpatterns = [
    url(r'^index',views.index,name="index"),
    url(r'^area/(?P<areaid>\d+)',views.area,name="area"),
    url(r'^problem/(?P<id>[0-9]+)',views.problem,name="problem"),
    url(r'^submit',views.submitproblem,name="submit"),
    url(r'^artificialproblems/',ArtificialProblemList.as_view()),
    ]
