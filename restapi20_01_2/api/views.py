from django.shortcuts import render
from api.serializers import StudentSerializer
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from api.models import Student
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPIView(View):
    def post(self,request):
        student_data=request.body
        stream=io.BytesIO(student_data)
        data=JSONParser().parse(stream)
        stud=StudentSerializer(data=data)
        if stud.is_valid():
            stud.save()
            return JsonResponse({'msg':'student created'},status=200)
        else:
            return JsonResponse({'msg':'error in creating student'},status=400)
def put(self,request):
    student_data=request.body
    stream=io.BytesIO(student_data)
    data=JSONParser().parse(stream)
    stud_instance=Student.objects.get(rollno=data['rollno'])
    stud=StudentSerializer(stud_instance,data)
    if stud.is_valid():
        stud.save()
        return JsonResponse({'msg':'updated...'},status=200)
    else:
        return JsonResponse({'msg':'error in uddate'},status=400)
def delete(self,request):
    student_data=request.body
    stream=io.BytesIO(student_data)
    data=JSONParser().parse(stream)
    try:
        stud_instance=Student.object.get(rollno=data['rollno'])
        stud_instance.delete()
        return JsonResponse({'msg':'student deleted...'},status=200)
    except:
        return JsonResponse({'msg':'invalid rollno...'},status=400)
def get(self,request):
    student_data=request.body
    stream=io.BytesIO(student_data)
    data=JSONParser().parse(stream)
    rollno=data.get('rollno',None)
    if rollno==None:
        qs=Student.objects.all()
        stu_dict=StudentSerializer(qs,many=True)
        return JsonResponse(stud_dict.data,safe=False)
    else:
        try:
            stud=Student.objects.get(rollno=rollno)
            stud_dict=StudentSerializer(stud)
            return JsonResponse(stud_dict.data,safe=False)
        except:
            return JsonResponse({'msg':'invalid rollno'},safe=False)

        