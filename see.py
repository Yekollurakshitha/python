a=str(input('enter the string: '))

str=''
index = 0
while index < len(a):
    str=str+a[index]
    if index != len(a)-1:
        str = str + "#"
    index += 1
print(str)
    
