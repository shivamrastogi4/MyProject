import sys
# def fact(n):
#     sum1=1
#     while(n>0):
#         sum1*=n
#         n-=1
#     return sum1
#
# num=fact(6)
# print(num)


                    #using recursion
n=int(input("Enter a number "))
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
sum = 1;
def fact(n):
    global sum
    globals()['sum']*=n
    n -= 1
    if(n>0):
       fact(n)
    return sum

sum=fact(n)
print(sum)

