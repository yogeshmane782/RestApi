import requests

BASE_URL="http://localhost:8000/"
END_POINT="createstudent/"

rollno=int(input("Enter Rollno"))
name=input("Enter Name")
course=input("Enter course")
fee=float(input("Enter Fee"))
stud={'rollno':rollno,
      'name':name,
      'course':course,
      'fee':fee}
response=requests.post(BASE_URL+END_POINT,data=stud)
stutuscode=response.status_code
if stutuscode==200:
    print(response.json())
else:
    print(response.json())