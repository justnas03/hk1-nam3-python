from Employee import *

class Intern(Employee):

    Majors = ''
    Semester = ''
    University_name = ''


    def __init__(self, ID, Fullname, BirthDay, Phone, Email, Employee_type, Majors, Semester, University_name):
            super().__init__(ID, Fullname, BirthDay, Phone, Email, Employee_type)
            self.Majors = Majors
            self.Semester = Semester
            self.University_name = University_name

    def showMe(self):
        if Employee.getID(self) != '':
            print(f"Majors: {self.Majors}")
            print(f"Semester: {self.Semester}")
            print(f"University Name: {self.University_name}")
        else:
            print("No Information for this instance")

    # def showInfo(self):
    #     super().showInfo()
    #     print(f"Majors: {self.Majors}")
    #     print(f"Semester: {self.Semester}")
    #     print(f"University Name: {self.University_name}")
