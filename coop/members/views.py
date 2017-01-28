from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from rest_framework.permissions import IsAdminUser


from guide.models import ArtificialProblem



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
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    


@user_passes_test(lambda u:hasattr(u,'member'))
def my_artificial_problems(request):
    order_by = request.GET.get('order_by','grade')
    queryset = ArtificialProblem.objects.filter(owner=request.user.member).order_by(order_by)
    return render(request,'members/my_artificial_problems.html',{
        'queryset':queryset,
        'ob':order_by,
        })
