import requests
import json

data={'rollno':8,
      'name':'kiran',
      'course':'mysql',
      'fee':2000}
json_data=json.dumps(data)
response=requests.post("http://localhost:8000/api/",data=json_data)
print(response)

