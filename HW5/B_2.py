import os
os.system("cls")


class MyComplexNumber:
    def __init__(self):
        pass

    def input(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

    def __str__(self):
        if self.imag_part > 0:
            return f"{self.real_part}+{self.imag_part}i"
        return f"{self.real_part}{self.imag_part}i"


if __name__ == "__main__":
    cn = MyComplexNumber()
    cn.input(10,-2)
    
    print(cn)    