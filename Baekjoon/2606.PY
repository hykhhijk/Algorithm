node = int(input())
edge = int(input())
num=0

graph = [[]for _ in range(node+1)]
visited=[False]* (node+1)

for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

    

def dfs(graph, start, visited):
    global num
    visited[start] = True
    num = num+1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph,1,visited)
print(num-1)