from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # the model i want 
        model = User
        # the field i want not all fields in user
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password' : {'write_only':True}}
        
    def create(self, validated_data):
        # validated data coming from the request object
        user = User.objects.create_user(**validated_data)
        return user