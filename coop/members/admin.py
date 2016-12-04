from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


from members.models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User,CustomUserAdmin)
