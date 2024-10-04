class Employee(object):
    Employee_count = 0  
    
    def __init__(self, ID, Fullname, BirthDay, Phone, Email, Employee_type):
        self.ID = ID
        self.Fullname = Fullname
        self.BirthDay = BirthDay
        self.Phone = Phone
        self.Email = Email
        self.Employee_type = Employee_type
        Employee.Employee_count += 1  
    
    def showInfo(self):
        print(f"ID: {self.ID}")
        print(f"Fullname: {self.Fullname}")
        print(f"BirthDay: {self.BirthDay}")
        print(f"Phone: {self.Phone}")
        print(f"Email: {self.Email}")
        print(f"Employee_type: {self.Employee_type}")
        
    def totalOfEmployee():
        print(f"Total of Employee: {Employee.Employee_count}")