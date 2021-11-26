import random
for i in range(1,11):
     a=random.randint(-10,10)
     print(a,'end=')
     if a>6:
         break
print()
print('First number>6',a,'on position',i)
