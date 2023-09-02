import sys
from itertools import permutations

n = int(input())
mat = [[] for _ in range(n+1)]
for i in range(n):
    mat[i] = list(map(int, sys.stdin.readline().split()))

nums = [i for i in range(n)]
perm = permutations(nums, n)


result = 997654321
first = mat[0][0]
for i in perm:
    if i[0]!=first:
        break
    temp = 0
    index = first
    for j in range(1, len(i)):
        if mat[index][i[j]]==0:
            temp = 987654321
            break
        temp += mat[index][i[j]]
        index = i[j]
    if mat[index][first]==0:
        temp = 987654321
    temp += mat[index][first]
    if temp < result:
        result = temp

print(result)