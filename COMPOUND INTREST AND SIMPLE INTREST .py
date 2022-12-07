#today's fourth program 8/9/2022
a=int(input('enter the amount:'))
b=int(input('enter the rate:'))
SI=a*b*0.02
M=a*(1+(b/100))**2
CI=M-a
print('compound intrest is :',CI)
print('simple intrest is:',SI)

