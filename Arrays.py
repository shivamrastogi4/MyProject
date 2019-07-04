from array import *
vals=array('i',[5,9,8,4,2]) #creating array, we need two things for it-- 1- type of array and values of array
num=vals.__len__() #gives length we can also use num=len(vals)
array1=vals.__copy__() #this also copies array inbuilt function
print(array1)
print("length of array is "+str(len(vals)))


#array printing using while
i=0
while i<len(vals):
    print(vals[i],end=" ")
    i+=1
print()

#array printing using while
for e in vals:
    print(e,end=" ")
print()

#copying array into new array
newArr=array(vals.typecode,(pow(a,3) for a in vals))
for e in newArr:
    print(e,end=" ") 