import numpy as np

# list1=[1, 2, 3, 4, 5]
# list2=[6, 7, 8, 9, 10]

# arr=np.array([list1,list2],dtype='float32')
# print("Array from list1 and list2:")
# print(arr)

# print(arr.ndim)   # number of dimensions
# print(arr.shape)  # rows, columns
# print(arr.size)   # total elements
# print(arr.dtype)  # data type



# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# list3 = [11, 12, 13, 14, 15]

# arr = np.array([list1, list2,list3])

# print(arr[0:2,3:5])


# #creating a list of 5 horsepower values
# horsepower = [130, 165, 150, 150, 140]
# #creating a numpy array from horsepower list
# horsepower_arr = np.array(horsepower)
# x = np.where(horsepower_arr >= 150)
# print(x) # gives the indices 
# # With the indices , we can find those values 
# horsepower_arr[x]


#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
#creating filter array
filter_arr = horsepower_arr > 135
newarr = horsepower_arr[filter_arr]
print(filter_arr)
print(newarr)
