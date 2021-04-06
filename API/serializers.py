from django.contrib.auth.models import User
from .models import Members
from rest_framework import serializers


class MembersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'about']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
