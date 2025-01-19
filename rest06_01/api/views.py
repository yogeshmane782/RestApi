from django.shortcuts import render
from django.views.generic import View
from api.models import Product
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
import json
# Create your views here.
class CreateProductView(View):
    def post(self,request,*args,**kwargs):
        print(request.POST)
        prodid=int(request.POST['prodid'])
        pname=request.POST['pname']
        price=float(request.POST['price'])
        p=Product.objects.create(prodid=prodid,pname=pname,price=price)
        p.save()
        d1={'msg':'Product Created...'}
        response=JsonResponse(d1)
        return response
class UpdateProductView(View):
    def put(self,request,*args,**kwargs):
        data=request.body
        data=data.decode()
        list1=data.split("&")
        dict1={}
        for value in list1:
            k,v=value.split("=")
        old_prod=Product.objects.get(prodid=int(dict1['prodid']))
        old_prod.prodid=int(dict1['prodid'])
        old_prod.pname=dict1['pname']
        old_prod.price=float(dict1['price'])
        old_prod.save()
        response=JsonResponse({'msg':'updated product'})
        return response
class DeleteView(View):
    def delete(self,request,*args,**kwargs):
        data=request.body
        data=data.decode()
        k,v=data.split('=')
        prod=Product.objects.get(prodid=int(v))
        prod.delete()
        response=JsonResponse({'msg':'Product deleted...'})
        return response
class ProductListView(View):
    def get(self,request,*args,**kwargs):
        qs=Product.objects.all()
        json_data=serialize("json",qs)
        product_list=json.loads(json_data)
        product_data=[]
        for row in product_list:
            prod={'prodid':row['pk'],'pname':row['fields']['pname'],'price':row['fields']['price']}
            product_data.append(prod)
            json_data=json.dumps(product_data)
            response=HttpResponse(json_data,content_type="application/json")
            return response
class ProductInfoView(View):
    def get(self,request,prodid,*args,**kwargs):
        product=Product.objects.get(prodid=prodid)
        json_data=serialize("json",[product])
        product_list=json.loads(json_data)
        product_data=[]
        for row in product_list:
            prod={'prodid':row['pk'],'pname':row['fields']['pname'],'price':row['fields']['price']}
            product_data.append(prod)
            json_data=json.dumps(product_data)
            response=HttpResponse(json_data,content_type="application/json")
            return response