from django.contrib import admin
from django.urls import reverse

from django.conf import settings
from django.utils.html import format_html,mark_safe

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



class FlagFilter(admin.SimpleListFilter):
    title = 'has_flag'
    parameter_name = 'flag'

    def lookups(self, request, model_admin):
        return [('True','True'),('False','False')]

    def queryset(self,request,queryset):
        if self.value():
            id_list = [ p.id for p in queryset if str(p.has_unresolved_flag())==self.value()]
            return queryset.filter(id__in=id_list)
        else:
            return queryset



class ArtificialProblemAdmin(admin.ModelAdmin):
    list_filter = ('exists','approved','area','grade','sector','owner',FlagFilter)
    list_display = ('area','grade','holds','sector','owner','links_to_flags')
    inlines = [ProblemImageInline,CommentInline,ProblemVideoInline]
    def links_to_flags(self,obj):
        urfs = obj.problemflag_set.filter(resolved=False)
        if urfs.count() == 0:
            return 'None'
        else: 
            lnks = [ "<a href = '{l}'>link</a>".format(l=reverse('admin:guide_problemflag_change',args=(fl.id,))) for fl in urfs]

            return mark_safe(",".join(lnks))

    def has_flag(self,obj):
        return  obj.problemflag_set.filter(resolved=False).count >0



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
admin.site.register(Comment)
admin.site.register(ProblemVideo)

