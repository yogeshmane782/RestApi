import json
import requests

stud_data={'rollno':2,'name':'kishore','course':'oracle','fee':200}
stud_json=json.dumps(stud_data)
response=requests.post("http://localhost:8000/create/",data=stud_json)
print(response.json())

stud_data={'rollno':10}
stud_json=json.dumps(stud_data)
response=requests.get("http://localhost:8000/get_one_stud/",data=stud_json)
print(response.json())

response=requests.get("http://localhost:8000/get_all/")
print(response.json())

stud_data={'rollno':2,
           'fee':7000}
stud_json=json.dumps(stud_data)
response=requests.put("http://localhost:8000/update_stud/",data=stud_json)
print(response.json())


