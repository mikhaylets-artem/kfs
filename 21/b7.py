n=int(input('n'))
s=0
    for i in range(n,2*n+1):
        x=i**2
        s+=x
        print(i,':',s)
    print('s=',s)
