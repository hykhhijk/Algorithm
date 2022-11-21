from collections import deque
import sys

node, edge, start = map(int, input().split())
graph = [[]for _ in range(node+1)]
visited = [False] * (node+1)
for _ in range(edge):
    n,m = map(int,sys.stdin.readline().split())
    graph[n].append(m)
    graph[m].append(n)



def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    if len(graph[start]) > 1: graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node= queue.popleft()
        print(node, end=" ")
        if len(graph[node]) > 1: graph[node].sort()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


dfs(graph, start, visited)
print()
visited = [False] * (node+1)
bfs(graph, start, visited)