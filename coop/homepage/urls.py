from django.conf.urls import url
from homepage import views

urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^index',views.index,name='index'),
        url(r'^about',views.about,name='about'),
        ]

