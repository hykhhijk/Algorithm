import sys
import math

n,m = list(map(int, input().split()))

result=[]

for i in range(n):
    result.append(0)

for i in range(n, m+1):
    if i==1 or i==2:
        result.append(0)
    else:
        result.append(i)
for i in range(n, m+1):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            result[i]=0
            break
for i in range(len(result)):
    if result[i]!=0:
        sys.stdout.write(str(result[i]) + "\n")