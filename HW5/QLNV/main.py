import os
os.system("cls")
from Employee import *
from Emp_Experience import *

if __name__ == "__main__":
    
    emp = Employee("E001", "John Doe", "1990-01-01", "123456789", "john.doe@example.com", 0)
    exp = Experience("E002", "Jane Doe", "1992-01-01", "987654321", "jane.doe@example.com", 1,3, "Java")
    emp.showInfo()
    print("")
    exp.showInfo()

    Employee.totalOfEmployee()