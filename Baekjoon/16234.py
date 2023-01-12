import sys
sys.setrecursionlimit(10**5)

N, L, R = map(int, input().split())
mat = []
for i in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))
visited = [[False]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def dfs(row, col, cnt):
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        elif visited[nx][ny]==False and L <= abs(cnt - mat[nx][ny]) <= R:
            visited[nx][ny]=True
            temp.append([nx, ny])
            dfs(nx, ny, mat[nx][ny])
    return 0

cnt=0
def move(x):
    for row in range(N):
        for col in range(N):
            if visited[row][col]==False:
                dfs(row, col, mat[row][col])
                if len(temp) > 0:
                    sum = 0
                    for i in range(len(temp)):
                        sum += mat[temp[i][0]][temp[i][1]]
                    for i in range(len(temp)):
                        mat[temp[i][0]][temp[i][1]] = sum//len(temp)
                    while temp:
                        temp.pop()
                    x=True
    if x==True:
        return 1
    else:
        return 0


while True:
    temp=[]
    visited = [[False]*N for _ in range(N)]
    result = move(False)
    if result==0:
        break
    else:
        cnt += result
print(cnt)
