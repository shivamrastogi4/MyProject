from numpy import *
arr=array([1,2,3])
print(arr.dtype) #will tell type of values stored in array
print(arr[0])
arr1=array([1.0,2,3]) #here implicit conversion occurs and all values are converted to float
print(arr1)
arr2=array([1.0,2,3],int) #explicit conversion to int of float value too
print(arr2)

##second method of creating array using linspace()
arr3=linspace(0,50,2) #bydefault 50 parts or step will be made else how many parts we define will be made
print(arr3) #linspace(startpoint,endpoint,no of parts it is to be divided)

##third method of creating array using arange()
arr4=arange(1,20,6) #arange(start, stop , step i.e. which number of element needs to be printed  after each step like in this after 1,
#6th element is 7 and after 7, 6th element is 13th )
print(arr4) #bydefault step value in arange is 1

#fourth method of creating array using logspace()
arr5=logspace(1,40,2) #logspace(startpoint,endpoint,no of parts it is to be divided but depends upon log of sstart and end point)
print(arr5)  #bydefault in step 50 parts will be divided

#fifth method of creating arrays using zeros()
arr6=zeros(5,int)
print(arr6)

#sizth method using ones()
arr7=ones(5,int)
print(arr7)