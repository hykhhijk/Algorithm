import sys
from math import inf

n = int(input())
m = int(input())
mat =[[]for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result_mat = [inf for _ in range(n+1)]
for _ in range(m):
    start_, end_, distance = map(int, sys.stdin.readline().split())
    mat[start_].append([end_, distance])
start, end = map(int, input().split())

def smallest():
    small = inf
    index = 0
    for j in range(len(result_mat)):
        if visited[j]==False and result_mat[j] < small:
            small = result_mat[j]
            index = j
    return index


def dijkstra(x):
    visited[x]=True
    result_mat[x] = 0
    for i in mat[x]:
        if result_mat[i[0]] < i[1]:
            continue
        else:
            result_mat[i[0]] = i[1]
    for i in range(n-1):
        node = smallest()
        visited[node] = True
        for j in mat[node]:
            if result_mat[j[0]] > j[1]+result_mat[node]:
                result_mat[j[0]] = j[1]+result_mat[node]

dijkstra(start)
print(result_mat[end])