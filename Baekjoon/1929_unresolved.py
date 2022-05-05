import sys

n,m = list(map(int, input().split()))

result=[]

for i in range(n):
    result.append(0)

for i in range(n, m+1):
    result.append(i)

for i in range(n, m+1):
    for j in range(2, i//2+1):
        if i%j == 0:
            result[i]=0
            break
for i in range(len(result)):
    if result[i]!=0:
        sys.stdout.write(str(result[i]) + "\n")