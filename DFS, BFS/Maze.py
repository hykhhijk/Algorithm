from collections import deque
n,m = map(int, input().split())
mat=[]
count=0

for _ in range(n):
    mat.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    queue= deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if mat[nx][ny]==0:
                continue
            if mat[nx][ny]==1:
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx, ny))
    return mat[n-1][m-1]

print(bfs(0, 0))



