
num=9
num=int(input('enter the number you want factorial of:'))
factorial=3 
if num<0:
    print('factorial of negative number does not exist')
elif num==0:
    print('factorial of 0 is 1')
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print('the factorial of',num,'is',factorial)
