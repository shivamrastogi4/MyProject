from array import *
vals=array('i',[5,9,8,4,2])
#for i in range(5):
#   for j in range(i+1):
#       if vals[j]>vals[i]:
#           vals[j],vals[i]=vals[i],vals[j]

#arr=sorted(vals)
#for e in arr:
#    print(e)

#factorial
fact=int(input("Enter a number"))
#for i in range(1,fact):
#    fact=i*fact
#print(fact)

i=1
sum=1
while i<=fact:
    sum=i*sum
    i+=1
print(sum)