import os
os.system("cls")

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def getName(self):
        return self.name
    
    def getScore(self,i):
        return self.score[i-1]
    
    def inputScore(self, scores):
        self.score = scores

    def getAverage(self):
        return sum(self.score)/len(self.score)
    
    def getHighscore(self):
        return max(self.score)
    
    def obtainHBcheck(self):
        for diem in self.score:
            if diem > 4 and self.getAverage() > 8.0:
                return "Duoc HB"
        return "Khong duoc HB"

    def __str__(self):
        return f"Student: {self.name}, Number: {self.number}, Score: {self.score}"


if __name__ == "__main__":
   
    st = Student('John',23 )
    st.inputScore([8,8.9,7.8,1.0])
    print(st)
    print("Name: ", st.getName())
    print("First score: ", st.getScore(1))
    print("Average: ", st.getAverage())
    print("HocBong?: ",st.obtainHBcheck())
    print("MaxDiem: ",st.getHighscore())
    
    
