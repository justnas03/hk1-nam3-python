from Employee import *

class Experience(Employee):

    def __init__(self, ID, Fullname, BirthDay, Phone, Email, Employee_type, ExpInYear, ProSkill):
        super().__init__(ID, Fullname, BirthDay, Phone, Email, Employee_type)
        self.ExpInYear = ExpInYear
        self.ProSkill = ProSkill

    def showInfo(self):
        super().showInfo()
        print(f"ExpInYear: {self.ExpInYear}")
        print(f"ProSkill: {self.ProSkill}")
        

