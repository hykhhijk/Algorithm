from itertools import combinations

n, m = map(int, input().split())
temp = list(combinations([i+1 for i in range(n)], m))
temp.sort()
for i in temp:
    print(" ".join(map(str, i)))