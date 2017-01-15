from django.db import models
from django.core.mail import send_mail


from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def set_password(self,*args,**kwargs):
        result = super(User,self).set_password(*args,**kwargs)
        try:
            send_mail(
                    'user update',
                    'User with email {em} updated a password'.format(em=self.email),
                    'galwayclimberscoop@gmail.com',
                    ['galwayclimberscoop@gmail.com'],
                    fail_silently=True,
                    )
        except:
            pass
        return result


class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{fn} {ln}".format(fn=self.user.first_name,ln=self.user.last_name)


