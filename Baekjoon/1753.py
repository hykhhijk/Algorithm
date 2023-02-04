import sys
import heapq

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
result = [10**10 for _ in range(v+1)]

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

def dijkstra(x):
    result[x]=0
    q = []
    heapq.heappush(q, [0, x])
    while q:
        cost, x = heapq.heappop(q)
        if result[x] < cost:
            continue
        for i in graph[x]:
            if result[i[0]] > i[1] + result[x]:
                result[i[0]] = i[1] + result[x]
                heapq.heappush(q, [result[i[0]], i[0]])

dijkstra(start)
for i in result[1:]:
    if i==10**10:
        print("INF")
    else:
        print(i)