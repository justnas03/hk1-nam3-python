import pyspark
import numpy as np
import pandas as pd
import os
os.system("cls")

d = {
    "col1" : [5.1, 4.9, 4.7, 4.6, 5.0],
    "col2" : [3.5, 3.0, 3.2, 3.1, 3.6]
}

index = ["a", "b", "c", "d", "e"]

df = pd.DataFrame(data = d, index=index)

print(df)
print("1")
print(df["col1"]) #take all values at col1 return series
print("2")
print(df[[False, False, True, True, False]]) #reject row a,b,e take c,d return dataframe
print("3")
print(df.loc["c"]) #take all values at row with lable "c" return series
print("4")
print(df.iloc[1]) #take all values at row with index [1] return series
print("5")
print(df[0:3]) #take all values in slicing from 0 -> 2 ([0:3]) return dataframe
print("6")
print(df.iloc[[1]]) #take all values at row 1 return dataframe
print("7")
print(df.iloc[[2,1]]) #take all values at row 2 then row 1 return dataframe
print("8")
print(df.iloc[0,1]) #take values at location (0,1) return value
print("9")
print(df.iloc[[0,3],[0,1]]) #take value row 0 and row 3, column 0 and column 1 return dataframe
print("10") 
print(df.iloc[2:4, 0:]) #take value row from 2->3 and col 0->end return dataframe
