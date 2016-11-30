from django.conf.urls import url

from guide import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^problem/(?P<id>[0-9]+)',views.problem),
    ]
