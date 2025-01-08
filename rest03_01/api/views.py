from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
# Create your views here.
def view1(request):
    if request.method=="GET":
        return JsonResponse({'msg':'GET Request'})
    elif request.method=="POST":
        return JsonResponse({'msg':'POST Request'})
    elif request.method=="PUT":
        return JsonResponse({'msg':'PUT Request'})
    elif request.method=="PATCH":
        return JsonResponse({'msg':'PATCH Request'})
    elif request.method=="DELETE":
        return JsonResponse({'msg':'DELETE Request'})
    else:
        return JsonResponse({'msg':request.method})
class View2(View):
    def get(self,request,*vargs,**kwargs):
        return JsonResponse({'msg':'GET Request'})
    def post(self,request,*vargs,**kwargs):
        return JsonResponse({'msg':'POST Request'})
    def put(self,request,*vargs,**kwqrgs):
        return JsonResponse({'msg':'PUT Request'})
    def patch(self,request,*vargs,**kwargs):
        return JsonResponse({'msg':'PATCH Request'})
    def delete(self,request,*vargs,**kwargs):
        return JsonResponse({'msg':'DELETE Request'})