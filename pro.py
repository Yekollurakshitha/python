tea=0
coffee=0
samosa=0
def cost(t,c,s):
    c=7*t+9*c+15*s
    return c
print("press 't' for tea,'c' for coffee, 's' for samosa, '*' if done")
s=''
while s!='*':
    s=input('')
    if s=='t':
        a=int(input('number:'))
    elif s=='c':
        b=int(input('number: '))
    elif s=='m':
        c=int(input('number: '))
    elif s=='*':
        continue
    else:
        print('beep')
totalcost=cost(a+b+c)
print('your total cost is',totalcost,'thanks! visit us again!')
