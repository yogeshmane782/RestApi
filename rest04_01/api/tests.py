import requests

BASE_URL="http://localhost:8000/"
def list_employees():
    END_POINT="listemp"
    response=requests.get(BASE_URL+END_POINT)
    json_data=response.json()
    print(json_data)
def read_employee(empno):
    END_POINT="reademp/"+str(empno)
    response=requests.get(BASE_URL+END_POINT)
    json_data=response.json()
    print(json_data)
print("1. List Employee")
print("2. Display Employee")
opt=int(input("Enter your option"))
if opt==1:
    list_employees()
elif opt==2:
    empno=int(input("EmployeeNo"))
    read_employee(empno)
