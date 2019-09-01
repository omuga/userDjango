from rest_framework import serializers
from .models import User

#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model =  User
#        fields = ("id","username","password","email")
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 120)
    password = serializers.CharField(max_length = 50)
    email = serializers.EmailField(max_length = 254)

    class Meta:
        model =  User
        fields = ("id","username","password","email")

    def create(self, validated_data):
        return User.objects.create(**validated_data)

