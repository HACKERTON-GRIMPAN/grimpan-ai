from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from create_image import views

urlpatterns = [
    path('', views.user_list, name="user_list"), # views를 checker url에서 사용할 수 있게 경로 설정

]
