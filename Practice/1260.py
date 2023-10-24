import sys
from collections import deque

n, m, v = map(int, input().split())
mat = [[]for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    mat[start].append(end)
    mat[end].append(start)
for i in range(len(mat)):
    mat[i] = sorted(mat[i])
visited = [False for _ in range(n+1)]

dfs_list = []
def dfs(v):
    if visited[v]==False:
        visited[v]=True
        dfs_list.append(v)
        for i in mat[v]:
            if visited[i]==False:
                dfs(i)

dfs(v)

visited = [False for _ in range(n+1)]
q = deque([v])
visited[v]=True
bfs_list = []
while q:
    next = q.popleft()
    bfs_list.append(next)
    for i in mat[next]:
        if visited[i]==False:
            visited[i]=True
            q.append(i)

print(" ".join(map(str, dfs_list)))
print(" ".join(map(str, bfs_list)))