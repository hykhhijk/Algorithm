import math
n = input()

index = n[0]
result=0
for i in range(len(n)):
    if n[i] != index:
        result+=1
        index=n[i]
print(math.ceil(result/2))

