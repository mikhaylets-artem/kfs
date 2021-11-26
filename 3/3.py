a=int(input('a='))
b=int(input('b='))
n=0
for i in range(a+1,b-1):
    print(b,end=' ')
    b-=1
    n=n+1
print()
print('count number:',n )
