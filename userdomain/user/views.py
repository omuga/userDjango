from django.shortcuts import render
from rest_framework import  viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .tasks import verify_users_ids
from django.http import HttpResponse, Http404

class UserView(ListModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, pk = None):
        if pk:
            print(pk)
            user = get_object_or_404(User.objects.all(),pk = pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = User.objects.all()
        serializer = UserSerializer(users,many = True)
        return Response({"users": serializer.data})
    
    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data = user)
        if serializer.is_valid(raise_exception = True):
            user_saved = serializer.save()
        return Response({"success:" "User '{}' creates sucessfully".format(user_saved.username)})

      
    def update(self,instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' updated successfully".format(user_saved.username)})
    def delete(self, request, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        verify_users_ids.delay(user.id)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)},status=204)

    def validate(request,pk):
        try:
            user = User.objects.get(pk = pk)
            return HttpResponse(1)
        except User.DoesNotExist:
            return Http404(0)



