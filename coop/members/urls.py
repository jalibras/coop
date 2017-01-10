from django.conf.urls import url, include

from members import views


# override the default login to implement remember me
from django.contrib.auth.views import login




urlpatterns = [
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^profile/',views.profile,name='profile'),
    ]

