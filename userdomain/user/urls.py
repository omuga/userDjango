
from django.urls import path,include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('',views.UserView)
urlpatterns = [
    path('users/',views.UserView.as_view()),
    path('users/<int:pk>', views.UserView.as_view())
]