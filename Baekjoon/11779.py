import sys
from math import inf
import heapq
from copy import deepcopy

n = int(input())
m = int(input())
distance = [inf for _ in range(n+1)]
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
start, end = map(int, input().split())
route=[[]for _ in range(n+1)]

q = [[0, start, route[start]]]
distance[start]=0
while q:
    dist, now, now_route = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        if distance[i[0]] > distance[now] + i[1]:
            # if distance[i[0]] != inf:
                # route.pop()
            distance[i[0]] = distance[now] + i[1]
            route[i[0]] = deepcopy(now_route)
            route[i[0]].append(now)
            heapq.heappush(q, [distance[i[0]], i[0], route[i[0]]])

route[end].append(end)
print(distance[end])
print(len(route[end]))
print(" ".join(map(str, route[end])))