import os
os.system("cls")
import numpy as np

if __name__ == "__main__":
    x = np.array([x for x in range(1,11)])
    print("a) Kiểm tra kiểu dữ liệu của các phần tử trong mảng")
    print(type(x))
    print("b) Kiểm tra kích thước của mảng(trả về một tuple dạng(n,))")
    print(x.shape)
    