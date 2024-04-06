import sys
sys.setrecursionlimit(10**6)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


M, N, k = map(int, input().split())         #행, 열 순서로 입력 들어옴
mat = [[0 for _ in range(N)]for _ in range(M)]
for i in range(k):
    x1, y2, x2, y1 = map(int, sys.stdin.readline().split())
    y2 = M-y2
    y1 = M-y1
    for x in range(x1, x2):
        for y in range(y1, y2):
            mat[y][x] +=1 

def dfs(x, y):
    mat[x][y]=-1
    for i in range(4):
        nx = x + dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >=M or ny < 0 or ny >=N:
            continue
        if mat[nx][ny]==0:
            dfs(nx, ny)
            mat[x][y] += mat[nx][ny]
    return  mat[x][y]



answer = []
count = 0
for i in range(M):
    for j in range(N):
        if mat[i][j]==0:
            value = dfs(i, j)
            count+=1
            answer.append(-1 * value)
answer.sort()
print(count)
print(" ".join(map(str, answer)))