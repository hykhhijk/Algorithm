from collections import deque
import sys
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
########### Readline중요성을 다시 한번 실감하는 문제였다....#####################
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)




distance = [-1 for _ in range(n+1)]

def bfs(start):
    queue=deque()
    queue.append(start)
    distance[start] = 0
    while queue:
        city = queue.popleft()
        if distance[city] > k:
            break
        for i in graph[city]:
            if distance[i]==-1:
                distance[i] = distance[city]+1
                queue.append(i)

bfs(x)
if k not in distance:
    print(-1)
    sys.exit()
for i in range(len(distance)):
    if k == distance[i]:
        print(i)
