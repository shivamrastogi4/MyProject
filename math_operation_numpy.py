from numpy import *
#from array import *
#arr=array([(11,22,3,4),(1,2,3,4)])  @2D array
#print(arr)
#print(len(arr))
#print(arr.ndim)
arr1=array([1,2,3,4,5])
arr=array([11,22,3,41,5])
print(arr1+arr) #this is also called as vectorize operation
                #using numpy it will add both array element wise but if we will not use numpy it will simply give a third array
                #which have values of both array like array('i',[1,2,3,4,5,1,2,3,4,5])
print(arr+5) #add 5 to each element of array available in numpy cannot be done by basic array import
print([arr<4]) #print boolean results of all elements greater then given condition
print(arr[arr<4]) #give array of all the values that satisfy given condition
print(arr/2)
print(arr*2)
print(arr1*arr)
print(sin(arr))
print(sqrt(arr1+arr))
print(square(arr1+arr))
print(median(arr1))
print(average(arr))
print(sorted(arr))
print(concatenate([arr,arr1]))
arr2=arr1 #copies one array to other array but still we have only one array and both arrays points to same array
print(id(arr2))
print(id(arr1))

arr2=arr1.view() #will create other array having different memory size
print(id(arr2))
