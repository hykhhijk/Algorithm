import sys
sys.setrecursionlimit(10**6)
from collections import deque

t = int(input())

def bfs(q):
    while q:
        node, case = q.popleft()
        # if visited[node]==0:
            # visited[node]=case
        for i in range(len(mat[node])):
            if visited[mat[node][i]]==0:
                q.append([mat[node][i], case*-1]) 
                visited[mat[node][i]] = case*-1
            elif visited[mat[node][i]]==case:
                return False
    return True


for _ in range(t):
    v, e = map(int, input().split())
    mat = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]     #0:not visited 1:case 1, -1: case 2
    for _ in range(e):
        start, end = map(int, sys.stdin.readline().split())
        mat[start].append(end)
        mat[end].append(start)

    result=1
    for i in range(1, len(visited)):
        if visited[i]==0:
            q = deque([[i,1]])
            visited[i]=1
            result *= int(bfs(q))
    if result==1:
        print("YES")
    else:
        print("NO")


