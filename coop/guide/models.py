from django.db import models
from django.conf import settings
from django.utils.html import format_html

# Create your models here.


class Problem(models.Model):

    name=models.CharField(max_length=300,null=True,blank=True)
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
            ('vert','vertical'),
            ('slov','slight overhang'),
            ('over','overhang'),
            ('exov','extreme overhang'),
            ('na','not applicable'),
            )
    steepness=models.CharField(max_length=50,choices=STEEPNESS_CHOICES,null=True,blank=True)
    holds=models.CharField(max_length=300,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    picture_1=models.FileField(upload_to='uploads',blank=True,null=True)
    picture_2=models.FileField(upload_to='uploads',blank=True,null=True)
    picture_3=models.FileField(upload_to='uploads',blank=True,null=True)
    video_snippets=models.CharField(max_length=1000,default='',null=True,blank=True)
    comments=models.TextField(blank=True,null=True)
    date=models.DateField(null=True,blank=True)
    setter=models.CharField(max_length=300,null=True,blank=True)
    exists=models.BooleanField(default=True)

    def pictures(self):
        raw_list = [
                self.picture_1,
                self.picture_2,
                self.picture_3,
                ]
        pic_list = list(filter(lambda x:x.name!='',raw_list))

        ht=""
        for pic in pic_list:
            try:
                im_url = settings.MEDIA_URL+pic.name
            except:
                return 'upload a picture'
            ht += "<p><img src='{url}' width='100%'/>".format(url=im_url)
        return format_html(ht)

    def videos(self): # THIS NEEDS TO BE FIXED
        try:
            raw = ("{pref}"+self.video_snippets+"{postf}").format(pref='<p>',list_separator='<p>',postf='')
            return format_html(raw)
        except:
            return format_html(self.video_snippets)



