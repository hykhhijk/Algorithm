import sys
from collections import deque
import math

dirs = [[-1, 0], [1, 0], [0,-1], [0,1]]
m, n = map(int, input().split())
mat = []
for _ in range(n):
    temp = sys.stdin.readline().strip()
    mat.append([int(i) for i in temp])
visited = [[math.inf for _ in range(m)] for _ in range(n)]
visited[0][0]=0

queue = deque([[0, 0]])

while queue:
    x, y = queue.popleft()
    for dir in dirs:
        nx = x+dir[0]
        ny = y+dir[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        else:
            if mat[nx][ny]==1:      #벽일때
                if visited[x][y]+1 < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx, ny])
            else:
                if visited[x][y] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]
                    queue.append([nx, ny])
print(visited[-1][-1])