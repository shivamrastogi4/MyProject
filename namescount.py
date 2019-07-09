#program to take 10 names and print names whose length is less than 5
def name_lengt(list):
    for i in list:
        if len(i)<=5:
            print(i)
        else:
            continue

print("Enter the 10 names of users")
name_row=[]
#for i in range(0,10):
i=0
while(i<10):
    x=input()
    name_row.append(x)
    i+=1

name_lengt(name_row)

