from django.contrib import admin

from django.conf import settings
from django.utils.html import format_html

from guide.models import ArtificialProblem,NaturalProblem,Area,ProblemImage,AreaImage,ProblemVideo,Comment,Sector,ProblemByMember,ProblemFlag

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class ProblemImageInline(admin.StackedInline):
    model = ProblemImage
    readonly_fields=['display']

class ProblemVideoInline(admin.StackedInline):
    model = ProblemVideo

class AreaAdmin(admin.ModelAdmin):
    pass

class ArtificialProblemAdmin(admin.ModelAdmin):
    list_filter = ('exists','approved','area','grade','sector','owner')
    list_display = ('area','grade','holds','sector','owner')
    inlines = [ProblemImageInline,CommentInline,ProblemVideoInline]


class NaturalProblemAdmin(admin.ModelAdmin):
    list_filter = ('area','grade','sector')
    list_display = ('area','grade','sector')
    inlines = [ProblemImageInline,CommentInline,ProblemVideoInline]


class ProblemFlagAdmin(admin.ModelAdmin):
    list_display= ('id','problem','issue','resolved','created')
    list_filter = ('issue','resolved')


admin.site.register(ArtificialProblem,ArtificialProblemAdmin)
admin.site.register(NaturalProblem,NaturalProblemAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Sector)
admin.site.register(AreaImage)
admin.site.register(ProblemImage)
admin.site.register(ProblemFlag,ProblemFlagAdmin)
admin.site.register(ProblemByMember)
