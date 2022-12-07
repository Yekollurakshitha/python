#to get grade of a student
a=int(input('enter the marks of first subject'))
b=int(input('enter the marks of second subject'))
c=int(input('enter the marks of third subject'))
d=int(input('enter the marks of fourth subject'))
e=int(input('enter the marks of fifth subjetc'))
avg=(a+b+c+d+e)/5
if (avg>=75 and avg<=100):
    print('EXCELLENT!')
elif(avg>=60 and avg<=75):
    print('FIRST CLASS ')
elif(avg>=55 and avg<=60):
    print('SECOND CLASS')
elif(avg>=33 and avg<=55):
    print('third class')
elif(avg>100 or avg<0):
    print('dimag kharab hai kya bhosdike')
else:
    print('fail hogaya hai tu')
