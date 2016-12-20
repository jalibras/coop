from django.db import models


from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{fn} {ln}".format(fn=self.user.first_name,ln=self.user.last_name)


