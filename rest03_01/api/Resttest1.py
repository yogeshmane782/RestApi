import requests
response=requests.get("http://localhost:8000/view1/")
json_data=response.json()
print(json_data)
response=requests.post("http://localhost:8000/view1/")
json_data=response.json()
print(json_data)
response=requests.put("http://localhost:8000/view1/")
print(response.json())
response=requests.patch("http://localhost:8000/view1/")
print(response.json())
response=requests.delete("http://localhost:8000/view1/")
print(response.json())
response=requests.options("http://localhost:8000/view1/")
print(response.json())
response=requests.get("http://localhost:8000/view2/")
json_data=response.json()
print(json_data)
response=requests.post("http://localhost:8000/view2/")
json_data=response.json()
print(json_data)
response=requests.put("http://localhost:8000/view2/")
print(response.json())
response=requests.patch("http://localhost:8000/view2/")
print(response.json())
response=requests.delete("http://localhost:8000/view2/")
print(response.json())





