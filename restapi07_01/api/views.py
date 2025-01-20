from django.shortcuts import render
from django.views.generic import View
from api.forms import StudentForm
from django.http import HttpResponse
import json 
# Create your views here.
class CreateStudView(View):
    def post(self,request,*args,**kwargs):
        stud=StudentForm(request.POST)
        try:
              if stud.is_valid():
                stud.save(commit=True)
                response=HttpResponse(json.dumps({'msg':'student created'}),content_type="application/json",status=200)
        except:
            response=HttpResponse(json.dumps({'msg':'error in creating student'}),content_type="application/json",status=400)                
        return response 

