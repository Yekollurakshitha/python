n=int(input('enter the number :'))

s=0

t=n
while t>0:
    digit=t%10
    s+=digit**3
    t//=10

if n==s:
    print(n,'is an armstrong number')
else:
    print(n,'is not an armstrong number')
