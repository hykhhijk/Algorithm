import sys
import heapq
from math import inf

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
index = 0
while True:
    n = int(input())
    if n==0:
        break
    graph = [[] for _ in range(n)]
    distance = [[inf]*n for _ in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        graph[i] = temp
    q = [[graph[0][0], 0, 0]]
    distance[0][0] = graph[0][0]
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                continue 
            if distance[nx][ny] > distance[x][y] + graph[nx][ny]:
                distance[nx][ny] = distance[x][y] + graph[nx][ny]
                heapq.heappush(q, [distance[nx][ny], nx, ny])
    index+=1            
    print(f"Problem {index}: {distance[-1][-1]}")
    