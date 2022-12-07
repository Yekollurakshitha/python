name=input('enter the name:')
index=0
a_count=0
while index<len(name):
    if name[index]=='a':
        a_count=a_count+1
    index=index+1
print("the frequency of 'a' in",name , "is:",a_count)
