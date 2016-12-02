from django.conf.urls import url
from homepage import views

urlpatterns = [
        url(r'^index',views.index,name='index'),
        ]

