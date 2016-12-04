from django.conf.urls import url, include

from members import views

urlpatterns = [
    url(r'^',include('django.contrib.auth.urls')),
    ]

