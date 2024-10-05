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

    def showInfo(self):
        if Employee.getID(self) != '':
            super().showInfo()
            print(f"Graduation_date: {self.Graduation_date}")
            print(f"Graduation_rank: {self.Graduation_rank}")
            print(f"Education: {self.Education}")
        else:
            print("No Information for this instance")

    def __str__(self):
        return f"ID: {self.ID}, Fullname: {self.Fullname}, BirthDay: {self.BirthDay}, Phone: {self.Phone}, Email: {self.Email}, Employee_type: {self.Employee_type}, Graduation_date: {self.Graduation_date}, Graduation_rank: {self.Graduation_rank}, Education: {self.Education}"

    