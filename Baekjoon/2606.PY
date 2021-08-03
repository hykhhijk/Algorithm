n = int(input())
m = int(input())


graph=[[] for _ in range(n+1)]
count = 0
visited = [False]*(n+1)


for i in range(m):
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)

def dfs(node):
    global count
    visited[node] =True
    if not graph[node]:
        return False
    for i in graph[node]:
        if visited[i] == False:
            dfs(i)
            count +=1



dfs(1)
print(count)