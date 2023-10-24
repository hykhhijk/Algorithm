import sys
import math
from collections import deque

n = int(input())
m = int(input())
buses = [[]for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    buses[start].append([end, cost])
start, end = map(int, input().split())
dist = [math.inf for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dist[start] = 0
# visited[start] = True
# queue = deque([start, 0])

# while queue:
def smallest():
    value=math.inf
    index = 0
    for i in range(len(buses)):
        if visited[i]==False:
            if dist[i] < value:
                value = dist[i]
                index = i
    return index

while True:
    start = smallest()
    if start == end or start==0:
        break
    visited[start] = True
    for i in range(len(buses[start])):
        if visited[buses[start][i][0]] == False and dist[buses[start][i][0]] > dist[start] +  buses[start][i][1]:
            dist[buses[start][i][0]] = dist[start] + buses[start][i][1]
                # queue.append(buses[start][i][0])

print(dist[end])