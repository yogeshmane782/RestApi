from django.shortcuts import render
from django.http import HttpResponse
import json
import xml.etree.ElementTree as ET
# Create your views here.
def text_output(request):
    msg="<h1>This is text message</h1>"
    response=HttpResponse(msg,content_type="text/plain")
    return response
def html_output(request):
    response=HttpResponse()
    response.write("<p>This is Paragraph</p>")
    response.write("<p> This is Paragraph2</p>")
    return response
def header_output(request):
    response=HttpResponse()
    response.write("<p> This is Paragraph1</p>")
    response.write("<p> This is Paragraph2</p>")
    return response
def attach_output(request):
    msg="Attachment"
    response=HttpResponse(msg,headers={"content_type":"application/vnd.ms-excel","Content-Disposition":'attachment;filename="Book1.xlsx"'})
    return response
def json_output(request):
    student_data=["naresh","ramesh","suresh","kishore","kiran"]
    json_data=json.dumps(student_data)
    response=HttpResponse(json_data,content_type="text/json")
    return response
def xml_output(request):
    users_list=["Nareshit","Arka","Computer Science","Engineer","Portal"]
    usrconfig=ET.Element("usrconfig")
    for user in range(len(users_list)):
        usr=ET.SubElement(usrconfig,"usr")
        usr.text=str(users_list[user])
    tree=ET.ElementTree(usrconfig)
    tree.write("output.xml",encoding="utf-8",xml_declaration=True)
    response=HttpResponse("")
    return response
