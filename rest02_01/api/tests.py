import requests

import requests
n1=int(input("Enter first number "))
n2=int(input("Enter second number "))
BASE_URL="http://localhost:8000/"
END_POINT="add1?n1="+str(n1)+"&n2="+str(n2)
response=requests.get(BASE_URL+END_POINT)
json_data=response.json()
print(f'result is {json_data["num3"]}')
