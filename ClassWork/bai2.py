import os
os.system("cls")

L = ["CNTT,20,600", "Ly,18,200", "Toan,19,100", "Hoa,19,150"]


k = dict()
for khoa in L:
    key = khoa.split(",")[0]
    value = khoa.split(",")[2]
    k[key] = int(value)
print(k)

s = sum(k.values())
print(s)


slsv = max(list(k.values()))
for key, value in k.items():
    if value == slsv:
        print(key)




    
