def person(name,age): #when u define variable for storing values these are formal arguments
   print(name)
   print(age-5)

person('shivam',6)  #position       #these are actual arguments as we are passing actual values


#actual arguments are of 4 types:
# 1- Position (if there are 10 args then we need to take care of positions we cant exchange the position) eg. person('shivam',6)
# 2- keyword (person(age=20,name='shivam') i.e. we are using keyword i.e we are mentioning variable name itself
# 3- default (i.e we are not passing some value and want that to be set by default) def person(name,age=18):
# imp-- 4-variable length (it is used like for example we add two values in calc and do + and + so it keeps on adding those values
# then in below function say we are passing 4 values sum(5,6,30,2) in place of 2 and want the sum of all 4 values )
#you can define a function where number of aruments are not fixed

def sum(*a):  #sde sum(a,*b) #*b says we can have multiple values
    #c=a+b       # will give cant add tuple to int error so will change it in next line
    c=0
    for i in a:
        c+=i
    print(a)
    print(c)


sum(5,6,3,4) ## this will give error  for def sum(a,b): as 5 will be assigned to a and remaining to b i.e. it will form
            # a tuple for all other values after a but will not give error for def sum(*a): as *a means we can have multiple
            #values for a and after iterating the whole values from tuple we can do whatever we needs.


def sum(*a):
    tup=a
    length=len(tup)
    count=0
    c=0
    print(length)
    for i in tup:
        if(i.isnumeric()):
            print(i+' is numeric')
        elif i.isalpha():
            print(i, end=" ")
    print()

sum('2','47','5','shivam','is','a','good','boy')

