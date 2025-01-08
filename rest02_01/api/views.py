from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def add_view(request):
    num1=int(request.GET['n1'])
    num2=int(request.GET['n2'])
    num3=num1+num2
    response=render(request,"app1/output.html",context={'num3':num3})
    return response
def home_view(request):
    response=render(request,"app1/calc.html")
    return response
def add_view1(request):
    num1=int(request.GET['n1'])
    num2=int(request.GET['n2'])
    num3=num1+num2
    json_data={'num3':num3}
    response=JsonResponse(json_data)
    return response
