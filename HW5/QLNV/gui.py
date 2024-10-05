from controller import *
import os

def Menu():
    list_emp = []

    print("Welcome to the Employee Management System")
    while True:
        print("Menu:")
        print("1. Add Employee")
        print("2. Print Employees")
        print("3. Clear Screen")
        print("4. Total Employess")
        print("5. Exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            os.system("cls")
            print(" ") 
            print("Add Employee selected")
            list_emp.append(AddEmployee())
        elif choice == 2:
            os.system("cls")
            print(" ") 
            print("Print Employees selected")
            for emp in list_emp:
                emp.showInfo()
                print(" ")       
        elif choice == 3:
            os.system("cls")
        elif choice == 4:
            os.system("cls")
            print(" ") 
            Employee.totalOfEmployee()
        elif choice == 5:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")