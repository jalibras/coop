from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


from members.models import User, Member

# Register your models here.

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User,CustomUserAdmin)
admin.site.register(Member)

