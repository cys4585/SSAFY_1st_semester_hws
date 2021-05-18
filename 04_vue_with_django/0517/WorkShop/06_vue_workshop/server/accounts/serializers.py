from django import db
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # json <-> db
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
