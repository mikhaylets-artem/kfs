a=float(input('a'))
b=float(input('b'))
s=1
if a<b:
    for i in range(a,b+1):
        s*=i
        print(i,":",s)
    print('S=',s)
else:
    print('error')
