from django.conf.urls import url

from guide import views



from guide.views import ArtificialProblemList



urlpatterns = [
    url(r'^index',views.index,name="index"),
    url(r'^area/(?P<areaid>\d+)',views.area,name="area"),
    url(r'^problem/(?P<id>[0-9]+)',views.problem,name="problem"),
    url(r'^problem/toggle/(?P<userid>[0-9]+)/(?P<problemid>[0-9]+)',views.toggle_problem_status,name="toggle"),
    url(r'^problem/getstatus/(?P<userid>[0-9]+)/(?P<problemid>[0-9]+)',views.get_problem_status,name="getstatus"),
    url(r'^submit/(?P<problem_type>(natural)|(artificial))',views.submitproblem,name="submit"),
    url(r'^update/(?P<problem_id>\d+)',views.submitproblem,name="update"),
    url(r'^artificialproblems/',ArtificialProblemList.as_view()),
    url(r'^artificialproblems/',ArtificialProblemList.as_view()),

    ]
