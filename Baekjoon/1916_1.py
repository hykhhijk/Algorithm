import sys
from math import inf

n = int(input())
m = int(input())

distance_mat = [[]for _ in range(n+1)]
mat = [inf for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    start, end, dist = map(int, sys.stdin.readline().split())
    distance_mat[start].append([end, dist])
start, end = map(int, input().split())

def smallest():
    small = inf
    index=0
    for i in range(len(mat)):
        if visited[i]==False and mat[i] < small:
            small = mat[i]
            index = i
    return index


mat[start] = 0
for i in range(n):
    node = smallest()
    # if node==inf:
        # break
    visited[node] = True
    for j in range(len(distance_mat[node])):
        if mat[node] + distance_mat[node][j][1] <  mat[distance_mat[node][j][0]]:
            mat[distance_mat[node][j][0]] = mat[node] + distance_mat[node][j][1]

print(mat[end])