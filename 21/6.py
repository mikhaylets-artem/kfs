n=int(input('n'))
s=0

if n>0:
    for i in range(1,n+1):
        s=1/i
        print(i,':',s)
    print('s=',s)
