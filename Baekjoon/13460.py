import sys
import collections

N, M = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(sys.stdin.readline().strip()))
# visited_r = [[False]*M for _ in range(N)]
# visited_b= [[False]*M for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
rx, ry, bx, by = 0, 0, 0, 0
queue = collections.deque([])
for i in range(N):
    for j in range(M):
        if mat[i][j]=="R":
            rx, ry = i, j
        if mat[i][j]=="B":
            bx, by = i, j
queue.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by]=True

def move(x, y, dirx, diry):
    dist = 0
    while mat[x+dirx][y+diry]!="#" and mat[x][y]!="O":
        x, y = x+dirx, y+diry
        dist+=1
    return x, y, dist

def search():
    while queue:
        rx, ry, bx, by, count= queue.popleft()


        for i in range(4):
            nrx, nry, rdist = move(rx, ry, dx[i], dy[i])
            nbx, nby, bdist = move(bx, by, dx[i], dy[i])
            # print(nrx, nry, nbx, nby, count)

            if count > 10:
                # print(nrx, nry, nbx, nby, count)
                print(-1)
                return 0
            else:
                if mat[nbx][nby] !="O":
                    if mat[nrx][nry] == "O":
                        print(count)
                        return 0
                    if nrx==nbx and nry==nby:
                        if rdist > bdist:
                            nrx, nry = nrx - dx[i], nry - dy[i]
                        else:
                            nbx, nby = nbx - dx[i], nby - dy[i]
                    if visited[nrx][nry][nbx][nby]==False:
                        visited[nrx][nry][nbx][nby]=True
                        # visited_r[nrx][nry] = True
                        # visited_b[nbx][nby] = True
                        queue.append([nrx, nry, nbx, nby, count+1])
    print(-1)
search()