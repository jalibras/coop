from django.conf.urls import url

from guide import views

urlpatterns = [
    url(r'^index',views.index),
    ]
