from django.shortcuts import render
from django.core.serializers import serialize
from api.models import Employee
from django.http import JsonResponse
import json
# Create your views here.
def list_employee(request):
    qs=Employee.objects.all()
    json_data=serialize("json",qs)
    dict1=json.loads(json_data)
    data=[]
    for row in dict1:
        qs=Employee.objects.all()
