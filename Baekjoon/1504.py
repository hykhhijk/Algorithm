import sys
import heapq
from math import inf


n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
target1, target2 = map(int, input().split())

def dijkstra(start, end):
    distance = [inf for _ in range(n+1)]
    q = [[0, start]]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if distance[i[0]] > distance[now] + i[1]:
                distance[i[0]] = distance[now] + i[1]
                heapq.heappush(q, [distance[i[0]], i[0]])
    return inf

result1 = 0
result1 += dijkstra(1, target1)
result1 += dijkstra(target1, target2)
result1 += dijkstra(target2, n)
result2= 0
result2 += dijkstra(1, target2)
result2 += dijkstra(target2, target1)
result2 += dijkstra(target1, n)

result = min(result1, result2)
if result >= inf:    
    print(-1)
else:
    print(result)