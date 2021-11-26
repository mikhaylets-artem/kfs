n=int(input('n'))
s=1
for i in range(1,n+1):
        x=(1+i*0.1)**(i+1)
        s+=x
        print(x,':',s)
print('s=',s)
