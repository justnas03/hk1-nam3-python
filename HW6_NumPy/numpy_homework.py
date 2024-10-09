import os
os.system("cls")
import numpy as np


if __name__ == "__main__":
    x = np.array([x for x in range(1,11)])
    print("a) Kiểm tra kiểu dữ liệu của các phần tử trong mảng")
    print(type(x))
    print("b) Kiểm tra kích thước của mảng(trả về một tuple dạng(n,))")
    print(x.shape)
    print("c) Tính mảng y và z sao cho y[i] = pi/2 - x[i] và z[i] = cos(x[i]) - sin(x[i])")
    y = np.pi/2 - x
    z = np.cos(x) - np.sin(x)
    print("Y=", y)
    print("Z=", z)
    print("d) Tìm những số chẵn/lẻ/số nguyên tố trong mảng.")
    bool_idx = (x%2==0)
    print(x[bool_idx])
    print("e) Thay thế các số chẵn trong mảng bằng -1, các số lẽ trong mảng bằng -2")
    t = np.where(bool_idx, -1, -2)
    print(t)