import sys
from collections import deque


m, n, h = map(int, input().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]



mat = []
for _ in range(h):
    floor = []
    for _ in range(n):
        floor.append(list(map(int, sys.stdin.readline().split())))
    mat.append(floor)
ripens=deque([])
visited = [[[False for _ in range(m)]for _ in range (n)] for _ in range(h)]


for floor in range(h):
    for row in range(n):
        for col in range(m):
            if mat[floor][row][col]==1:
                ripens.append([floor, row, col])
                visited[floor][row][col] = True


while ripens:
    z, x, y = ripens.popleft()
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i] 
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nz][nx][ny]==True or mat[nz][nx][ny]==-1:
            continue
        if mat[nz][nx][ny]==0:
            mat[nz][nx][ny] = mat[z][x][y] + 1
            ripens.append([nz, nx, ny])

def check():
    result = 0
    for floor in range(h):
        for row in range(n):
            for col in range(m):
                if mat[floor][row][col]==0:
                    return -1
                elif mat[floor][row][col] > result:
                    result = mat[floor][row][col]
    return result-1
print(check())
                