import itertools
n, m = map(int, input().split())

result = 1
for i in range(n, n-m, -1):
    result *= i

for j in range(1, m+1, 1):
    result = result//j

print(int(result))