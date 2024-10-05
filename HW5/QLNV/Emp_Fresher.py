from Employee import *

class Fresher(Employee):

    Graduation_date = ''
    Graduation_rank = ''
    Education = ''

    def __init__(self, ID, Fullname, BirthDay, Phone, Email, Employee_type, Graduation_date, Graduation_rank, Education):
            super().__init__(ID, Fullname, BirthDay, Phone, Email, Employee_type)
            self.Graduation_date = Graduation_date
            self.Graduation_rank = Graduation_rank
            self.Education = Education

    def showMe(self):
        if Employee.getID(self) != '':
            print(f"Graduation_date: {self.Graduation_date}")
            print(f"Graduation_rank: {self.Graduation_rank}")
            print(f"Education: {self.Education}")
        else:
            print("No Information for this instance")


    # def showInfo(self):
    #     super().showInfo()
    #     print(f"Graduation_date: {self.Graduation_date}")
    #     print(f"Graduation_rank: {self.Graduation_rank}")
    #     print(f"Education: {self.Education}")