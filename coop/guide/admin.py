from django.contrib import admin

from django.conf import settings
from django.utils.html import format_html

from guide.models import ArtificialProblem,NaturalProblem,Area,ProblemImage


# Register your models here.

class ProblemImageInline(admin.StackedInline):
    model = ProblemImage

class AreaAdmin(admin.ModelAdmin):
    pass

class ArtificialProblemAdmin(admin.ModelAdmin):
    list_filter = ('grade','steepness')
    list_display = ('grade','holds','steepness')
    inlines = [ProblemImageInline]


class NaturalProblemAdmin(admin.ModelAdmin):
    list_filter = ('grade','steepness')
    list_display = ('grade','steepness')
    inlines = [ProblemImageInline]
    pass




admin.site.register(ArtificialProblem,ArtificialProblemAdmin)
admin.site.register(NaturalProblem,NaturalProblemAdmin)
admin.site.register(Area,AreaAdmin)
