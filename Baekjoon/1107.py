n = int(input())
m = int(input())

if m==0:
    broken = []
else:
    broken = list(map(int, input().split()))
channel = 100
index  = False

result = abs(100 - n)

for i in range(1000000):
    for j in str(i):
        if int(j) in broken and index==False:
            index = True
            break
    if index==False:
        result = min(result, len(str(i)) + abs(n-i))
    index=False

print(result)