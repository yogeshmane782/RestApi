from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from api.models import Student
from api.serializers import StudentSerializer
# Create your views here.
class StudenCreateAPIView(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentUpdateAPIView(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentListAPIView(ListAPIView):
    queryset=Student.objects.all()
    serilizer_class=StudentSerializer
class StudentDestroyAPIView(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieveAPIView(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



