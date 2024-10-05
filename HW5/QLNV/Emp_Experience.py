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
            print(f"ExpInYear: {self.ExpInYear}")
            print(f"ProSkill: {self.ProSkill}")
        else:
            print("No Information for this instance")

    # def showInfo(self):
    #     super().showInfo()
    #     print(f"ExpInYear: {self.ExpInYear}")
    #     print(f"ProSkill: {self.ProSkill}")
        

