import random
name=str(input("enter your name:"))
counter=1
while counter<=10:
    index=random.randint(0,len(name)-1)
    print(name[index])
    counter=counter+1

