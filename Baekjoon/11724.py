from collections import deque
import sys


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, sys.stdin.readline().split(" "))
    graph[start].append(end)
    graph[end].append(start)


visited = [False for _ in range(n+1)]

def dfs(start):
    queue=deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

result = 0
for i in range(1, len(visited)):
    if visited[i]==False:
        dfs(i)
        result+=1

print(result)