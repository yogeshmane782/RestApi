"""
URL configuration for restapi21_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('student/create/',StudenCreateAPIView.as_view(),name='studentcreate'),
    path('student/update/<pk>',StudentUpdateAPIView.as_view(),name='studentcreate'),
    path('student/update/<pk>/',StudentUpdateAPIView.as_view(),name='studentupdate'),
    path('studentlist/',StudentListAPIView.as_view(),name='studentlist'),
    path('studentdelete/<pk>/',StudentDestroyAPIView.as_view(),name='studentdelete'),
    path('student/<pk>',StudentRetrieveAPIView.as_view(),name='studentretrieve'),
    path('student/<pk>/',StudentRetrieveUpdateDestroyAPIView.as_view(),name='student')

]
