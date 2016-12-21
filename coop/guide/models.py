from django.db import models
from django.conf import settings
from django.utils.html import format_html

from members.mixins import PermissionMixin
from members.models import Member


# Create your models here.


class Area(models.Model,PermissionMixin):
    name=models.CharField(max_length=300,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    area_map_image=models.FileField(upload_to='uploads',null=True,blank=True)
    area_map_imagemap_snippet=models.TextField(null=True,blank=True)
    area_type=models.CharField(max_length=15,choices=(('natural','natural'),('artificial','artificial')),default='artificial')
    def video_count(self):
        return ProblemVideo.objects.filter(problem__area=self).count()


    def __str__(self):
        return self.name

class BaseProblem(models.Model,PermissionMixin):
    area=models.ForeignKey('Area',null=True,blank=True)
    FONT_GRADES=(
            ('?','?'),
            ('3','3'),
            ('3+','3+'),
            ('4','4'),
            ('4+','4+'),
            ('5','5'),
            ('5+','5+'),
            ('6A','6A'),
            ('6A+','6A+'),
            ('6B','6B'),
            ('6B+','6B+'),
            ('6C','6C'),
            ('6C+','6C+'),
            ('7A','7A'),
            ('7A+','7A+'),
            ('7B','7B'),
            ('7B+','7B+'),
            ('7C','7C'),
            ('7C+','7C+'),
            )
    grade=models.CharField(max_length=50,choices=FONT_GRADES,default='?',blank=True)
    STEEPNESS_CHOICES = (
            ('slab','slab'),
            ('vertical','vertical'),
            ('slightly overhanging','slightly overhanging'),
            ('overhanging','overhanging'),
            ('extremely overhanging','extremely overhanging'),
            ('not applicable','not applicable'),
            )
    steepness=models.CharField(max_length=50,choices=STEEPNESS_CHOICES,null=True,blank=True)
    #def steepness_func(self):
    #    return dict(list(self.STEEPNESS_CHOICES))[self.steepness]
    sector=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    exists=models.BooleanField(default=True)
    approved=models.BooleanField(default=True)
    owner=models.ForeignKey(Member,null=True,blank=True)

# methods for embedding media in the admin
# for the site this stuff should be in the templates
    def pictures(self):
        pic_list = self.problemimage_set.all()
        if len(pic_list)==0:
            return False

        ht=""
        for pic in pic_list:
            try:
                im_url = settings.MEDIA_URL+pic.image_file.name
            except:
                return 'upload a picture'
            ht += "<p><img src='{url}' width='100%'/>".format(url=im_url)
        return format_html(ht)



class ArtificialProblem(BaseProblem):
    date=models.DateField(null=True,blank=True)
    holds=models.CharField(max_length=300,null=True,blank=True)
    setter=models.CharField(max_length=300,null=True,blank=True)

class NaturalProblem(BaseProblem):
    name=models.CharField(max_length=300,null=True,blank=True)
    rock_type=models.CharField(max_length=50,null=True,blank=True)
    first_ascensionist=models.CharField(max_length=100,null=True,blank=True)


class Sector(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    area = models.ForeignKey(Area,null=True,blank=True)



class ProblemImage(models.Model,PermissionMixin):
    problem = models.ForeignKey(BaseProblem)
    image_file = models.FileField(upload_to='uploads',blank=True,null=True)

    # method for displaying in the admin 
    def display(self):
        if self.image_file.name:
            im_url = settings.MEDIA_URL+self.image_file.name
            ht = "<p><img src='{url}' width='100%'/>".format(url=im_url)
            return format_html(ht)
        else:
            return format_html('')



class Comment(models.Model,PermissionMixin):
    text = models.TextField()
    problem = models.ForeignKey(BaseProblem,null=True,blank=True)
    member = models.ForeignKey(Member,null=True,blank=True)
 
class ProblemVideo(models.Model,PermissionMixin):
    embed_code = models.CharField(max_length=1000)
    problem = models.ForeignKey(BaseProblem,null=True,blank=True)
    member = models.ForeignKey(Member,null=True,blank=True) 




class Send(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    problem = models.ForeignKey(BaseProblem,on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)



