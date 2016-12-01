from django.contrib import admin

from django.conf import settings
from django.utils.html import format_html

from guide.models import ArtificialProblem,NaturalProblem,Area


# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    pass

class ArtificialProblemAdmin(admin.ModelAdmin):
    list_filter = ('grade','steepness')
    list_display = ('grade','holds','steepness','picture_1')

    readonly_fields=('pictures','videos')
    
    def pictures(self,obj):
        raw_list = [
                obj.picture_1,
                obj.picture_2,
                obj.picture_3,
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

    def videos(self,obj): # THIS NEEDS TO BE FIXED
        try:
            raw = ("{pref}"+obj.video_snippets+"{postf}").format(pref='<p>',list_separator='<p>',postf='')
            return format_html(raw)
        except:
            return format_html(obj.video_snippets)

class NaturalProblemAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArtificialProblem,ArtificialProblemAdmin)
admin.site.register(NaturalProblem,NaturalProblemAdmin)
admin.site.register(Area,AreaAdmin)
