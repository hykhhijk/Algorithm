import sys
import collections

m, n = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
visited = [[0]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(temp):
    q = collections.deque(temp)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif mat[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx, ny])
    return 

temp=[]
for row in range(n):
    for col in range(m):
        if mat[row][col]==1 and visited[row][col]==0:
            temp.append([row, col])
            visited[row][col]=1
        elif mat[row][col]==-1:
            visited[row][col] = -1
dfs(temp)

            

result = set()
for i in visited:
    for j in i:
        result.add(j)
if 0 in result:
    print(-1)
else:
    print(max(result)-1)