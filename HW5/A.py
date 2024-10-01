import os
os.system("cls")

class HinhChuNhat(object):
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def getArea(self):
        return self.chieudai*self.chieurong
    
    def __str__(self) -> str:
        return f"HCN(cd={self.chieudai}, cr={self.chieurong})"
    
if __name__ == "__main__":
    hcn = HinhChuNhat(4,5)
    print(hcn)
    print(hcn.getArea())