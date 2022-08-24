from rest_framework import serializers
from users.models import User


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email',)
        model = User



class JWTTokenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'bio', 'email', 'role', 'first_name', 'last_name',
        )
        model = User


