from django.shortcuts import render

# Create your views here.



from rest_framework import viewsets

from members.models import User, Member
from members.serializers import UserSerializer, MemberSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
