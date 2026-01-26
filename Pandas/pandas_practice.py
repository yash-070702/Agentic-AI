import pandas as pd 
import numpy as np
data=[1,2,3,4,5,6,7,8]

dt=pd.Series(data=data)
print(dt)
print(dt[0])

dt=pd.Series(data=data , index=['a','b','c','d','e','f','g','h'])
print(dt)

dict1={
    'a':1,
    'b':2,
    'c':3
}
dict2={
    'd':4,
    'e':5,
    'c':6
}

print(dt[0:5])
print(dt['a':'d'])

print(dt.values)
print(dt.index)

print(dt['a'])


df=pd.DataFrame({'value1':dict1,'value2':dict2})


print(df)


dict3={
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88]
}

df=pd.DataFrame(data=dict3 , index=['a','b','c'])

print(df)

print(df['Name'])
print(df.tail(1))
print(df.head(2))

df.info()
df.shape
df.columns
