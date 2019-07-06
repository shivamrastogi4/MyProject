from array import *
vals=array('i',[])
num=int(input("Enter size of array"))
i=0
while i<num:
    number=int(input("Enter value"))
    vals.append(number)
    i+=1

sear=int(input("Enter number to be deleted"))
index=vals.index(sear)
print(index)
val1=array(vals.typecode,[])

for e in vals:
    if sear!=e:
        val1.append(e)
    else:
        continue
#print("Previous array before deleting is "+str(vals))
print("New Array is "+str(val1))

print(val1[::-1]) #other method to print array in reverse

list=[]     #using list creating a list and assigning all the values to list of that array
for i in val1:
    list.append(i)
#print(list)

val2=array(val1.typecode,[])

#print(list(4))
num=len(list)-1         #appending all the values of list in array starting from last so new array will be in reverse format
while num>=0:
    val2.append(list[num])
    num-=1

print("After reversal of new array"+str(val2))
