from Employee import *

class Experience(Employee):
    ExpInYear = ''
    ProSkill = ''

    def __init__(self, ID, Fullname, BirthDay, Phone, Email, Employee_type, ExpInYear, ProSkill):
        super().__init__(ID, Fullname, BirthDay, Phone, Email, Employee_type)
        self.ExpInYear = ExpInYear
        self.ProSkill = ProSkill

    def showMe(self):
        if Employee.getID(self) != '':
            super().showInfo()
            print(f"ExpInYear: {self.ExpInYear}")
            print(f"ProSkill: {self.ProSkill}")
        else:
            print("No Information for this instance")

    def showInfo(self):
        if Employee.getID(self) != '':
            super().showInfo()
            print(f"ExpInYear: {self.ExpInYear}")
            print(f"ProSkill: {self.ProSkill}")
        else:
            print("No Information for this instance")
    
    def __str__(self):
        return f"ID: {self.ID}, Fullname: {self.Fullname}, BirthDay: {self.BirthDay}, Phone: {self.Phone}, Email: {self.Email}, Employee_type: {self.Employee_type}, ExpInYear: {self.ExpInYear}, ProSkill: {self.ProSkill}"

