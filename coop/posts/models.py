from django.db import models

from members.models import Member
from guide.models import BaseProblem

# Create your models here.


class AbstractPost(models.Model):
    member = models.ForeignKey(Member,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VideoPost(AbstractPost):
    url = models.URLField()
    problem = models.ForeignKey(BaseProblem,null=True,blank=True) # a video might not be associated to a particular problem


class ProblemComment(AbstractPost):
    text = models.TextField(null=True,blank=True)
    problem = models.ForeignKey(BaseProblem)

