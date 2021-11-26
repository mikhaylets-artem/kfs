import random
for i in range(1,11):
    a=random.randint(-10,10)
    print(a,end=' ')
    if a<0:
        break
print()
print('first number:',a,'on position:',i)

