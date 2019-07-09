def listpass(list):
    even=[]
    evencount=0
    oddcount=0
    odd=[]
    for i in list:
        if(i%2==0):
            even.append(i)
            evencount+=1
        else:
            odd.append(i)
            oddcount+=1
    #print("even list is ",even,"and count is ",evencount)
    #print("odd list is ",odd,"and count is ",oddcount)
    return oddcount, evencount
lst=[1,2,3,4,5,6,7]
even,odd=listpass(lst)
print("Even number count is :{} and Odd number count is:{}".format(even,odd))