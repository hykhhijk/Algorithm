import sys
import collections

n, m = map(int, input().split())
mat = []
for i in range(n):
    mat.append(list(sys.stdin.readline()))
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    distance = 0
    visited = [[0]*m for _ in range(n)]
    q = collections.deque([[x, y]])
    visited[x][y]=1
    while q:
        x,y = q.popleft()   
        distance = visited[x][y]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif mat[nx][ny]=="L" and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])
    return distance



results=[]
for row in range(n):
    for col in range(m):
        if mat[row][col]=="L":
            results.append(bfs(row, col))
result = max(list(set(results)))
print(result-1)
