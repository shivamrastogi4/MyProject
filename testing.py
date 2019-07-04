from array import *
num=int(input("Enter aray size"))
vals=array('I',[])  #using I for unsigned i.e. all positive ints
i=0
while i<num:
    number=int(input("Enter value"))
    if number>=0:
        vals.append(number)
    else:
        print("array is only for positive numbers hence exiting...")
        break
    i+=1
sear=int(input("Enter number to be searched"))
count=0
for i in vals:
    if sear==i:
        print("Value found at index "+str(count+1))
        break
    else:
        count+=1

delete=int(input("Enter the number to be deleted "))
for i in vals:
    if delete==i:
        print("Value found at index "+str(count+1))
    else:
        count+=1
