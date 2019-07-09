c=1
a=10
print(id(a))
def fun():
    #global a    #for trewating a as global inside function
    a=8
    x=globals()['a']
    print(id(x))
    globals()['a']=1.1
    print(x)
    print("inside",a)
fun()
print("outside",a)
