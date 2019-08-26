from django.shortcuts import render
from rest_framework import  viewsets
from .models import Bookitem
from .serializers import BookItemSerializer

# Create your views here.
class BookItemView(viewsets.ModelViewSet):
    queryset = Bookitem.objects.all()
    serializer_class = BookItemSerializer