import random
n=int(input())
m=int(input())
a=[[random.randint(0,9) for j in range(m)] for i in range(n)]
b=[a[i][j] for i in range(n) for j in range(m) if i==j]
print(a)

print("-"*20)
for i in a:
    print(f"\t\t\t|{i}|")
print(b)
