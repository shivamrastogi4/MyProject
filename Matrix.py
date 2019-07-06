from numpy import *

arr = array([('shivam', 22, 3, 4), (1, 2, 3, 4)])
arr1 = array([
    [1, 2, 3, 4, 5, 6],
    [5, 6, 7, 8, 9, 10]
])
arr11 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

# print(arr.dtype) print(arr1.ndim) print(arr.shape)
print(arr.size)  # size of entire block i.e. how manny elements are present
# print(arr1.__sizeof__())
# how to create an array2 with all the elements of array 1 but arr2 will be 1D array
arr2 = arr1.flatten()
print(arr2)

arr3 = arr2.reshape(3, 4)  # reshape the arr2 array which is in 2D to give arr3 of size 3*4 3 rows and 4 columns
print(arr3)
# arr4=arr2.reshape(3,2,2) #it will create 3 subarrays of size 2*2 from arr2 which is 1D array of 12 elements
# (3,2,2) will have three 2D arrays and each 2D array will have 2 1D arrays and each 1D array will habe 2 values
# print(arr4)
# converting 2D array in matrix format
m = matrix(arr11)  # in this we can do matrix operations
print(m)
m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,2,3;4,5,6;7,8,9')
print(m1)
print(diagonal(m1)) #it prints diagonal elements of matrix
print(m1*m2)