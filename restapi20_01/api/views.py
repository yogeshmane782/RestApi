from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def create_student(request):
    student_data=request.body
    stream=io.BytesIO(student_data)
    data=JSONParser().parse(stream)
    stud=StudentSerializer(data=data)
    if stud.is_valid():
        stud.save()
        return JsonResponse({'msg':'student is created'},safe=False,status=200)
    else:
        return JsonResponse({'msg':'error in creating student'},safe=False,status=400)
def get_student(request):
    student_data=request.body
    stream=io.BytesIO(student_data)
    data=JSONParser().parse(stream)
    rollno=data.get('rollno')
    try:
        stud=Student.objects.get(rollno=rollno)
        stud_serializer=StudentSerializer(stud)
        return JsonResponse(stud_serializer.data)
    except:
        return JsonResponse({'msg':"invalid rollno"})
def get_all_students(requests):
    qs=Student.objects.all()
    stud_serializer=StudentSerializer(qs,many=True)
    stud_dict=stud_serializer.data
    return JsonResponse(stud_dict,safe=False)
@csrf_exempt
def update_student(requests):
      json_data=requests.body
      stream=io.BytesIO(json_data)
      stud_dict=JSONParser().parse(stream)
      try:
        stud=Student.objects.get(rollno=stud_dict.get('rollno'))
        stud=StudentSerializer(stud,stud_dict)
       
        return JsonResponse({'msg':'updated...'},safe=False,status=200)
      except:
            return JsonResponse({'msg':'error'},safe=False,status=400)
