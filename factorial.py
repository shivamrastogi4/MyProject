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


#sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())

                         #using recursion my haphazard way
# n=int(input("Enter a number "))
# sum = 1;
# def fact(n):
#     global sum
#     globals()['sum']*=n
#     n -= 1
#     if(n>0):
#        fact(n)
#     return sum
#
# sum=fact(n)
# print(sum)

#or
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)