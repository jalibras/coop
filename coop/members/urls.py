from django.conf.urls import url, include

from members import views


# override the default login to implement remember me
#from django.contrib.auth.views import login
#from django.contrib.auth.views import login,password_reset,password_change

from django.contrib.auth.views import password_reset





urlpatterns = [
    #url(r'password_reset',password_reset,{'template_name':'registration/my_password_reset_form.html'}),
    #url(r'password_change',password_change,{'template_name':'registration/my_password_change_form.html'}),
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^my_artificial_problems/',views.my_artificial_problems,name='my_artificial_problems'),
    ]

