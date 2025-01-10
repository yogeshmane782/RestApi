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
        row['fields']['empno']=row['pk']
        data.append(row['fields'])
    json_data=json.dumps(data)
    response=JsonResponse(json_data,safe=False)
    return response
def read_employee(request,empno):
    emp=Employee.objects.get(empno=empno)
    json_data=serialize("json",[emp])
    response=JsonResponse(json_data,safe=False)
    return response
