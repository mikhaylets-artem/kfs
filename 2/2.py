import random
p=1
k=5
for  i in range(10):
    a=random.randint(-10,10)
    print(a,end='')
    if a%k==0 and a!=0:
        p*=a
print()
print('p= ',p)
