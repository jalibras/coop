from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test


# Create your views here.



from rest_framework import viewsets

from members.models import User, Member
from members.serializers import UserSerializer, MemberSerializer

@user_passes_test(lambda u:hasattr(u,'member'))
def profile(request):
    member = request.user.member
    return render(request,'members/profile.html',
            {
                }
            )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
