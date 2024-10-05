class Employee(object):
    Employee_count = 0
    ID = ''
    Fullname = ''
    BirthDay = ''
    Phone = ''
    Email = ''
    Employee_type = ''  
    
    def __init__(self, ID, Fullname, BirthDay, Phone, Email, Employee_type):
        if Employee.checkVar(ID, Fullname, BirthDay, Phone, Email):
            self.ID = ID
            self.Fullname = Fullname
            self.BirthDay = BirthDay
            self.Phone = Phone
            self.Email = Email
            self.Employee_type = Employee_type
            Employee.Employee_count += 1  
        else: 
            print("Input Error")

    def getID(self):
        return self.ID

    def showInfo(self):
        if self.ID != '':
            print(f"ID: {self.ID}")
            print(f"Fullname: {self.Fullname}")
            print(f"BirthDay: {self.BirthDay}")
            print(f"Phone: {self.Phone}")
            print(f"Email: {self.Email}")
            if self.Employee_type == 0:
                print(f"Employee_type: Experience")
            elif self.Employee_type == 1:
                print(f"Employee_type: Fresher")
            else:
                print(f"Employee_type: Intern")
        else:
            return 

    def checkVar(ID, Fullname, BirthDay, Phone, Email):
        import re
        # Check BirthDay format
        birthDayPattern = r'^\d{1,2}/\d{1,2}/\d{4}$'  # Example: 12/12/1990
        if not re.match(birthDayPattern, BirthDay):
            return False
        
        # Check Email format
        emailPattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'  # Example: abc123@example.com
        if not re.match(emailPattern, Email):
            return False
        
        # Check Fullname
        fullnamePattern = r'^[a-zA-Z\s]+$' # Example: John Doe
        if not re.match(fullnamePattern, Fullname):
            return False
        
        # Check Phone number
        phonePattern = r'^\d+$'  # Example: 1234567890
        if not re.match(phonePattern, Phone):
            return False
        
        return True
        
    def totalOfEmployee():
        print(f"Total of Employee: {Employee.Employee_count}")