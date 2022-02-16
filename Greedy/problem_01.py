n = int(input())
m = list(map(int, input().split()))

m.sort()
count = 0
for _ in range(n):
    index = m[0]
    if m[0] > len(m):
        break
    for _ in range(index):
        del(m[0])
    count += 1

print(count)