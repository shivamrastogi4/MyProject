def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('shivam',age=28,city='khatima',mob=9627872378)   #keyworded variable length argument

def person(name,*data):
    print(name)
    for i in data:
        print(i)

person('shivam',28,'khatima',9627872378)  #variable length arument
a= input("Etner number")
print(a)