from rest_framework import serializers
from .models import Bookitem

class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Bookitem
        fields = ("id","titulo","descripcion","author")