from collections import deque

n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(n+1):
    graph[i].sort()
visited = [False]*(n+1)
temp = deque()

def dfs(i):
    visited[i] = True
    print(i, end=" ")
    if not graph[i]:
        return False
    for i in graph[i]:
        if visited[i] == False:
            dfs(i)

def bfs(i):
    print(i, end=" ")
    if not graph[i]:
        return False
    for i in graph[i]:
        if visited[i] == False:
            temp.append(i)
            visited[i] = True
    if not temp:
        return False
    bfs(temp.popleft())

 
dfs(k)
print("")
visited = [False]*(n+1)
visited[k]=True
bfs(k)