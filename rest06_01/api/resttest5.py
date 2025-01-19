import requests
import tkinter as gui
import json
import tkinter.messagebox
BASE_URL="http://localhost:8000/"
def create_product():
    window=gui.Tk()
    window.geometry("300x200+100+100")
    window.title("Add Product")
    l1=gui.Label(window,text="ProductID",font=("Arial",15))
    l2=gui.Label(window,text="ProductName",font=("Arial",15))
    l3=gui.Label(window,text="ProductPrice",font=("Arial",15))
    e1=gui.Entry(window,font=("Arial",15))
    e2=gui.Entry(window,font=("Arial",15))
    e3=gui.Entry(window,font=("Arial",15))
    def add():
        product={'prodid':int(e1.get()),
        'pname':e2.get(),
        'price':float(e3.get())}
        response=requests.post(BASE_URL+"createprod/",data=product)
        if response.status_code==200:
            data=response.json()
            tkinter.messagebox.showinfo(title='info',message=data['msg'])
        else:
            tkinter.messagebox.showerror(title="error",message="error creating product")
    def close():
        window.destroy()
    b1=gui.Button(window,text="Add",font=("Arial",15),command=add)
    b2=gui.Button(window,text="Close",font=("Arial",15),command=close)

    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    e3.grid(row=3,column=2)
    b1.grid(row=4,column=1)
    b2.grid(row=4,column=2)

def update_product():
    prodid=int(input("productid:"))
    pname=input("productname:")
    price=float(input("price:"))
    product={'prodid':prodid,'pname':pname,'price':price}
    response=requests.put(BASE_URL+"updateprod/",data=product)
    print(response)
def delete_product():
    prodid=int(input("ProductID:"))
    product={'prodid':prodid}
    response=requests.delete(BASE_URL+"deleteprod/",data=product)
    if response.status_code==200:
        print(response.json())
    else:
        print("invalid productid")
def product_list():
    response=requests.get(BASE_URL+"productlist")
    json_data=response.json()
    for row in json_data:
        print(row['prodid'],row['pname'],row['price'])
def product_info(prodid):
    response=requests.get(BASE_URL+"productinfo/"+str(prodid))
    if response.status_code==200:
        data=response.json()
        for row in data:
            print(row['prodid'],row['pname'],row['price'])
    else:
        print("invalid product id")

while True:
    print("1. Adding Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Product List")
    print("5. Product Info")
    print("6. Exit")
    opt=int(input("Enter Your Option:"))
    match(opt):
        case 1:
            create_product()
        case 2:
            update_product()
        case 3:
            delete_product()
        case 4:
            product_list()
        case 5:
            prodid=int(input("Enter ProductId"))
            product_info(prodid)
        case 6:
            break
        case _:
            print("invalid option")
            


