from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Marks
import json
# Create your views here.
def create_marks(request):
    rollno=int(request.POST['rollno'])
    sub1=int(request.POST['sub1'])
    sub2=int(request.POST['sub2'])
    s=Marks(rollno=rollno,sub1=sub1,sub2=sub2)
    s.save()
    d1={'msg':'marks created...'}
    response=JsonResponse(d1)
    return response
def findresult(request):
    rollno=request.GET['rollno']
    stud=Marks.objects.get(rollno=rollno)
    stud_dict={'sub1':stud.sub1,'sub2':stud.sub2}
    response=JsonResponse(stud_dict)
    return response
def updatemarks(request):
    rollno=int(request.POST['rollno'])
    sub1=int(request.POST['sub1'])
    sub2=int(request.POST['sub2'])
    stud=Marks.objects.get(rollno=rollno)
    stud.sub1=sub1
    stud.sub2=sub2
    stud.save()
    d1={'msg':'Marks Updated...'}
    response=JsonResponse(d1)
    return response
def deletemarks(request):
    rollno=int(request.POST['rollno'])
    stud=Marks.objects.get(rollno=rollno)
    stud.delete()
    msg={'msg':'marks deleted...'}
    response=JsonResponse(msg)
    return response

