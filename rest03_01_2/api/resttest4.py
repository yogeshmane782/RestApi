import requests

BASE_URL="http://localhost:8000/"
def create():
    rollno=int(input("Rollno:"))
    sub1=int(input("Subject1 Marks:"))
    sub2=int(input("Subject2 Marks:"))
    END_POINT=BASE_URL+"create/"
    stud={'rollno':rollno,'sub1':sub1,'sub2':sub2}
    response=requests.post(END_POINT,data=stud)
    print(response.status_code)
    if response.status_code==200:
        d1=response.json()
        print(d1['msg'])
    else:
        print("unable create student")

def findresult():
    rollno=int(input("Rollno"))
    d1={'rollno':rollno}
    END_POINT=BASE_URL+"findresult"
    response=requests.get(END_POINT,params=d1)
    if response.status_code==200:
        data=response.json()
        s1=data['sub1']
        s2=data['sub2']
        total=s1+s2
        avg=total/2
        result="PASS" if s1>=40 and s2>=40 else "FAIL"
        print(f'''ROLLNO {rollno}
        SUBJECT1 {s1}
        SUBJECT2 {s2}
        TOTAL {total}
        AVG {avg:.2f}
        RESULT {result}''')
    else:
        print("Invalid Rollno")

def updatemarks():
    rollno=int(input("Rollno:"))
    sub1=int(input("Subject1 Marks:"))
    sub2=int(input("Subject2 Marks:"))
    stud={'rollno':rollno,'sub1':sub1,'sub2':sub2}
    response=requests.post(BASE_URL+"updatemarks/",data=stud)
    if response.status_code==200:
        print(response.json())
    else:
        print("invalid rollno")
def delete_stud():
    rollno=int(input("Rollno"))
    response=requests.post(BASE_URL+"deletemarks/",data={'rollno':rollno})
    if response.status_code==200:
        print(response.json())
    else:
        print("invalid rollno")
while True:
    print("1.Adding Marks")
    print("2.Updating Marks")
    print("3.Delete Student")
    print("4.Find Result")
    print("5.Exit")
    opt=int(input("Enter Your Option"))
    match(opt):
        case 1:
            create()
        case 2:
            updatemarks()
        case 3:
            delete_stud()
        case 4:
            findresult()
        case 5:
             break
        case _:
            print("Invalid option")