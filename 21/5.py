a=int(input('a'))
b=int(input('b'))
s=0
if a<b:
    for i in range(a,b+1):
        s+=i**2
        print(i,":",i**2,':',s)
    print('S=',s)
else:
    print('error')
