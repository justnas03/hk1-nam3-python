import os
os.system("cls")


class MyComplexNumber:
    
    def __init__(self, real_part=0, imag_part=0):
        self.real_part = real_part
        self.imag_part = imag_part
   
    def input(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

    def my_addition(self, other):
        real = self.real_part + other.real_part
        imag = self.imag_part + other.imag_part
        result = MyComplexNumber()
        result.input(real, imag)
        return result
    def __add__(self, other):
        real = self.real_part + other.real_part
        imag = self.imag_part + other.imag_part
        result = MyComplexNumber()
        result.input(real, imag)
        return result
    
    def my_subtraction(self, other):
        real = self.real_part - other.real_part
        imag = self.imag_part - other.imag_part
        result = MyComplexNumber()
        result.input(real, imag)
        return result
    def __sub__(self, other):
        real = self.real_part - other.real_part
        imag = self.imag_part - other.imag_part
        result = MyComplexNumber()
        result.input(real, imag)
        return result
    
    def my_multi(self, other):
        real = self.real_part*other.real_part - self.imag_part*other.imag_part
        imag = self.real_part*other.imag_part + self.imag_part*other.real_part
        result = MyComplexNumber()
        result.input(real, imag)
        return result
    def __mul__(self, other):
        real = self.real_part*other.real_part - self.imag_part*other.imag_part
        imag = self.real_part*other.imag_part + self.imag_part*other.real_part
        result = MyComplexNumber()
        result.input(real, imag)
        return result
    
    def my_div(self, other):
        try:
            real = (other.real_part*self.real_part + other.imag_part*self.imag_part)/(other.real_part**2 + other.imag_part**2)
            imag = (other.real_part*self.imag_part - other.imag_part*self.real_part)/(other.real_part**2 + other.imag_part**2)
            result = MyComplexNumber()
            result.input(round(real,2), round(imag,2))
            return result
        except Exception as e:
            print("Oops!", e.__class__," occured.")
            return "Can't be divided to Zero. check your Complex Numbers again!"
    def __truediv__(self, other):
        try:
            real = (other.real_part*self.real_part + other.imag_part*self.imag_part)/(other.real_part**2 + other.imag_part**2)
            imag = (other.real_part*self.imag_part - other.imag_part*self.real_part)/(other.real_part**2 + other.imag_part**2)
            result = MyComplexNumber()
            result.input(round(real,2), round(imag,2))
            return result
        except Exception as e:
            print("Oops!", e.__class__," occured.")
            return "Can't be divided to Zero. check your Complex Numbers again!"

    def moduleOf(self):
        import math
        return math.sqrt(self.real_part**2 + self.imag_part**2)

    def compareTo(self, other):
            print("\nCompare base of its module: ")
            if self.moduleOf() < other.moduleOf():
                print(f"{self}  < {other}")
            elif self.moduleOf() == other.moduleOf():
                print(f"{self} = {other}")
            else:
                print(f"{self} > {other}")            

    def __eq__(self, other):
        if self.moduleOf() == other.moduleOf():
            return True
        return False
    def __lt__(self, other):
        if self.moduleOf() < other.moduleOf():
            return True
        return False
    def __gt__(self, other):
        if self.moduleOf() > other.moduleOf():
            return True
        return False
    
    def __str__(self):
        if self.imag_part >= 0:
            return f"{self.real_part}+{self.imag_part}i"
        return f"{self.real_part}{self.imag_part}i"


if __name__ == "__main__":
    I = MyComplexNumber(10,2)
    J = MyComplexNumber()
    J.input(5,2)
    print(I); print(J)
    print()
    print("Addition: ", I.my_addition(J))
    print("Subtraction: ", I.my_subtraction(J))
    print("Multiplication: ", I.my_multi(J))
    print("Division: ", I.my_div(J))
    print()
    print("**Override Existed Operators")
    print("Addition: ", I+J)
    print("Subtraction: ", I-J)
    print("Multiplication: ", I*J)
    print("Division: ", I/J)

    I.compareTo(J)

    print(I == J)
    print(I < J)
    print(I > J)

    
 
  