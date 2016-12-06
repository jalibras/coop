from django.conf.urls import url, include

from members import views


# override the default login to implement remember me
from django.contrib.auth.views import login

def custom_login(*args,**kwargs):
    return login(*args,**kwargs)



urlpatterns = [
    url(r'login',custom_login),
    url(r'^',include('django.contrib.auth.urls')),
    ]

