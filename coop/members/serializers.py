from rest_framework import serializers

from members.models import Member, User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()

