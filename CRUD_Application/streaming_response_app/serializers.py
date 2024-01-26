from rest_framework import serializers
from .models import UserStream

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStream
        fields = '__all__'