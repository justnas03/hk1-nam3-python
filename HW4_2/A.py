import os
os.system("cls")

def bai1():
    vehicles = [
        ("Car",180),
        ("Bike",25),
        ("Plane",1000)
    ]
    vehicles = dict(vehicles)
    for key,value in vehicles.items():
        print(f"Vehicles: {key}, Speed = {value}")


def bai2():
    d = {'b':200, 'a':100, 'c':1}
    print(d['a'])
    print(d.get('e', None)) # get default
    print(len(d)) # count keys
    print(d.keys()) #list of keys
    print(d.values()) #list of values
    print(d.pop('b')) #del 1 key-value and return that value 
    print(d)


def bai3():
    d = {'b':200, 'a':100, 'c':1}
    d['b'] = -1*d.get('b') #Thay thế giá trị của khóa b thành số âm tương ứng.
    d['e'] =500 #Thêm một khóa 'e' có giá trị là 500 vào d 'e':500
    #del(d['b']) #Xóa khóa b ra khỏi từ điển (theo cách an toàn).

    #In các cặp (key,value) ra màn hình theo thứ tự từ điển.
    keys = list(d.keys())
    keys.sort()
    print(keys)
    for key in keys:
        print(f"{key}:{d[key]}")
    
if __name__ == "__main__":
    bai3()

