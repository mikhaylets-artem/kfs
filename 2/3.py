import random
s=0
for i in range(1,11):
    a=random.randint(-10,10)
    print(a,end=' ')
    if a%2!=0 and i%2==0:
        s+=a
print()
print('s=',s)
