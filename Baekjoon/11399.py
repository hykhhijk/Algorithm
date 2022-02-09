n = int(input())
m = list(map(int, input().split()))

m.sort()
result = 0
for index, value in enumerate(range(n)):
    result += m[value] * (n-index)
print(result)