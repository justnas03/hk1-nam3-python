import os
os.system("cls")

class Shape:
    def __init__(self):
        pass
    def getArea(self):
        return 0
    def __str__(self):
        return("Shape: ")

class HCN(Shape):
    def __init__(self,cd,cr):
        super().__init__()
        self.cd = cd
        self.cr = cr
    
    def getArea(self):
        return self.cd * self.cr

    def __str__(self):
        return super().__str__() + f" HCN({self.cd},{self.cr})"

class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.lenght = lenght
    
    def getArea(self):
        return self.lenght**2
    
    def __str__(self):
        return super().__str__() + f" Square({self.lenght})"

if __name__ == "__main__":
    sq = Square(5)
    hcn = HCN(5,10)
    print(sq)
    print(hcn)
    print(sq.getArea())
    print(hcn.getArea())
    
