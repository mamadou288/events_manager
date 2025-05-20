from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture', 'bio', 'location', 'date_of_birth']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            profile_picture=validated_data.get('profile_picture'),
            bio=validated_data.get('bio', ''),
            location=validated_data.get('location', ''),
            date_of_birth=validated_data.get('date_of_birth', None)
        )
        return user
