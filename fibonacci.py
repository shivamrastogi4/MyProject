def fibonacci(n):
    lst=[]
    i=0
    if n<0:
        print("Enter a valid number ")
    elif n==0:
        print("You got an empty list")
    else:
        a = 0
        b = 1
        lst.append(a)
        lst.append(b)
        while(i<n-2):
            c=a+b
            lst.append(c)
            a,b=b,c
            i+=1
    return lst

counter=input("How many numbers u want in fibonacci series: ")
lst=fibonacci(int(counter))
print("Fibonacci series of {} numbers is: ".format(counter))
print(lst)