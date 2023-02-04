import sys
import itertools

n = int(input())
sour = []
bitter = []
for _ in range(n):
    s, b = map(int, sys.stdin.readline().split())
    sour.append(s)
    bitter.append(b)


result = 10**10
for i in range(n):
    temp = list(itertools.combinations(range(n),i+1))
    for j in temp:
        temp_s = 1
        temp_b = 0
        for k in j:
            temp_s *= sour[k]
            temp_b += bitter[k]
            if result > abs(temp_s - temp_b):
                result = abs(temp_s - temp_b)
print(result)
