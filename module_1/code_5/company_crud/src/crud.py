from time import sleep
from src.utils import clear,pause,title
from src.data import data,save_company
from src.decorators import screen

@screen("Register company")
def register_company():
    ruc = input("Enter RUC : ")
    name = input("Enter Razon Social : ")
    add = input("Enter Dirección : ")
    
    data[ruc] = {
        "company_name":name,
        "direcction":add
    }
    title("Registered company")
    
@screen("Show companies") 
def show_company():
    for ruc,info in data.items():
        print(f"RUC : {ruc}")
        print(f"Company Name : {info['company_name']}")
        print(f"Direcction : {info['direcction']}")
        print("*" * 50)
        
@screen("Update company") 
def update_company():
    ruc = input("Enter company RUC : ")

    if ruc in data:
        print(f"Company located : {data[ruc]['company_name']}")
        print("Input new data or press ENTER to skip")

        new_name = input(f"New name ({data[ruc]['company_name']}): ")
        new_email = input(f"New email ({data[ruc]['direcction']}): ")

            
        data[ruc]["company_name"] = new_name if new_email else data[ruc]["company_name"]

        if new_email != "":
            data[ruc]["direcction"] = new_email

        print("Company updated...")
    else:
        print("Company not updated...")
        
@screen("Clear company")
def delete_company():
    ruc = input("Enter company RUC : ")

    if ruc in data:
        del data[ruc]
        print("Delete company")
    else:
        print("Company deleted")
        
def main_menu():
    while True:
        clear()
        title("COMPANY CRUD")
        print("""
            [1] REGISTER COMPANY
            [2] SHOW COMPANIES
            [3] UPDATE COMPANY
            [4] DELETE COMPANY
            [5] EXIT
        """)
        
        option = int(input("ENTER OPTION : "))
        
        if option == 1:
            register_company()
            pause()
        elif option == 2:
            show_company()
            pause()
        elif option == 3:
            update_company()
            pause()
        elif option == 4:
            delete_company()
            pause()
        elif option == 5:
            save_company(data)
            clear()
            title("Exiting system...")
            print("Data saved in company.csv")
            sleep(2)
            break
        else:
            print("Invalid option.")