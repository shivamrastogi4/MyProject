        # Using lambda inside a function

# def is_even(n):
#     return n%2==0
# def is_odd(n):
#     return n%2!=0
nums=[1,2,3,4,5,6,7,8,9,10,11]
#evens=list(filter(is_even,nums))
#odds=list(filter(is_odd,nums))
evens=list(filter(lambda n:n%2==0,nums))
odds=list(filter(lambda n:n%2!=0,nums))
print(odds)
print(evens)

        #using map
from functools import *
doubles=list(map(lambda n:n*2,nums))
print(doubles)
        #using reduce
sum= reduce(lambda a,b:a+b,doubles)
print(sum)

f=lambda a,b:a+b
lst=[1,2,3,4,5,6,7,8,9,10]
sum=reduce(f,lst)
print(sum)

f=lambda n:n*f(n-1)
#lst=[1,2,3,4,5,6,7,8,9,10]
#sum=reduce(f,lst)
fact=f(5)
print(fact)


