import os
os.system("cls")

class Dog(object):
    "This is dog class" #__doc__
    def __init__(self,name,ages):
        self.name = name
        self.ages = ages
    
    def sayHi(self):
        print(f"My name is {self.name}, I am {self.ages} years old")
    
if __name__ == "__main__":
    d1 = Dog('Lucky',3)
    d1.sayHi()