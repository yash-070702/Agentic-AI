# 🧪 NumPy Practice Dataset

# Assume the following dataset is already created in NumPy:

# import numpy as np

# data = np.array([
#     [12, 15, 18, 20],
#     [22, 25, 28, 30],
#     [32, 35, 38, 40],
#     [42, 45, 48, 50],
#     [52, 55, 58, 60]
# ])


# Shape of data → (5, 4)
# Think of it as 5 records × 4 features

# 📝 Practice Questions (NumPy Only)
# 🔹 Level 1: Basics

# What is the shape of the array?

# What is the data type (dtype) of the array?

# What is the total number of elements in the array?

# 🔹 Level 2: Indexing & Slicing

# Extract the 3rd row.

# Extract the 2nd column.

# Extract the sub-matrix:

# [[25, 28],
#  [35, 38],
#  [45, 48]]


# What is the last element of the array?

# 🔹 Level 3: Operations

# Add 10 to every element.

# Multiply only the first column by 2.

# Find the sum of each row.

# Find the mean of each column.

# 🔹 Level 4: Logical & Conditional

# How many elements are greater than 40?

# Extract all elements between 25 and 50 (inclusive).

# Replace all values greater than 45 with -1.

# 🔹 Level 5: Shape Manipulation

# Reshape the array into (4, 5) — is it possible? (Yes / No + Why)

# Flatten the array into 1D.

# What will be the shape after using data.



import numpy as np
data=np.array([
              [12, 15, 18, 20],
              [22, 25, 28, 30],
              [32, 35, 38, 40],
              [42, 45, 48, 50],
              [52, 55, 58, 60]
])
print(data.shape)
print(data.dtype)
print(data.size)
print(data[2])
print(data[:,1:2])
print(data[1:4,1:3])
print(data[-1,-1])
print(data+10)
print(data*[2,1,1,1])

list1=[]
for row in data:
    list1.append(row.sum())
print(list1)

print(np.mean(data,axis=0))

x=np.where(data>40)
y=data[x]
print(len(y))


at=np.where((data>=25) & (data<=50))
print(data[at])

new_data=data.copy()
new_data[new_data>45]=-1
print(new_data)

data=data.reshape(4,5)
print(data)

print(data.flatten())


#####################################
#####################################
#####################################
