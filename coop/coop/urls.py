"""coop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


from guide.views import area, ArtificialProblemViewSet,NaturalProblemViewSet,ProblemImageViewSet, AreaViewSet, SectorViewSet

from members.views import UserViewSet,MemberViewSet


admin.site.site_header='Galway Climbing Co-op admin'
admin.site.site_title='Galway Climbing Co-op admin'
#admin.site.index_title='Galway Climbing Co-op admin'


# django rest framework url routers for viewsets
router = routers.DefaultRouter()
router.register(r'artificialproblems',ArtificialProblemViewSet)
router.register(r'naturalproblems',NaturalProblemViewSet)
router.register(r'problemimages',ProblemImageViewSet)
router.register(r'users',UserViewSet)
router.register(r'members',MemberViewSet)
router.register(r'areas',AreaViewSet)
router.register(r'sectors',SectorViewSet)



from django.contrib.auth.views import password_reset

urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',area),
    url(r'^guide/', include('guide.urls',namespace="guide")),
    url(r'^home/', include('homepage.urls',namespace="homepage")),
    url(r'^members/auth/', include('members.urls')),
    # note that the (customised) templates for the auth views are in [BASE_DIR]/templates/registration
    url(r'^members/', include('members.urls',namespace="members")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
