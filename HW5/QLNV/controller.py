from Employee import *
from Experience import *
from Fresher import *
from Intern import *

def AddEmployee():
    emp = None
    ID = input("ID: ")
    Fullname = input("Fullname: ")
    BirthDay = input("BirthDay (dd/mm/yyyy): ")
    Phone = input("Phone: ")
    Email = input("Email: ")
    Employee_type = int(input("Employee Type (0 for Experience, 1 for Fresher, 2 for Intern, 3 Not Classified): "))
    if Employee_type == 0:
        ExpInYear = int(input("ExpInYear: "))
        ProSkill = input("ProSkill: ")
        emp = Experience(ID, Fullname, BirthDay, Phone, Email, Employee_type, ExpInYear, ProSkill)
    elif Employee_type == 1:
        Graduation_date = input("Graduation_date: ")
        Graduation_rank = input("Graduation_rank: ")
        Education = input("Education: ")
        emp = Fresher(ID, Fullname, BirthDay, Phone, Email, Employee_type, Graduation_date, Graduation_rank, Education)
    elif Employee_type == 2:
        Major = input("Major: ")
        Semester = input("Semester: ")
        University_name = input("University_name: ")
        emp = Intern(ID, Fullname, BirthDay, Phone, Email, Employee_type, Major, Semester, University_name)
    elif Employee_type == 3:
        emp = Employee(ID, Fullname, BirthDay, Phone, Email, Employee_type)
    return emp


