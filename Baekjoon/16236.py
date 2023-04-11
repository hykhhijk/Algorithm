import sys
import collections

N = int(input())

size = 2
fish = 0
mat = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def check(size):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if 0<mat[i][j]<size:
                return True
    return False



def bfs(q):
    temp=[]
    while q:
        row, col, size, dist = q.popleft()
        # if temp and dist <= temp[-1][0]:
        #     break
        for i in range(4):
            n_r, n_c = row+dx[i], col+dy[i]
            if n_r<0 or n_r>=N or n_c<0 or n_c>=N or visited[n_r][n_c]==True:
                continue
            elif mat[n_r][n_c]>size:
                continue
            elif 0<mat[n_r][n_c]<size:
                q.append([n_r, n_c, size, dist+1])
                temp.append([dist+1, n_r, n_c])
                visited[n_r][n_c]=True
            else:
                q.append([n_r, n_c, size, dist+1])
                visited[n_r][n_c]=True

    if len(temp)!=0:
        temp.sort()
        return temp[0]
    else:
        return -1

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if row[j]!=0:
            if row[j]==9:
                shark = [i, j, 2, 0]          #처음 크기는 2
            else:
                fish+=1

    mat.append(row)
mat[shark[0]][shark[1]]=0
size = shark[2]
queue = collections.deque([shark])
index=0
dist=0
next=-1
for _ in range(fish):
    visited = [[False]*N for _ in range(N)]

    next = bfs(queue)
    if next==-1:
        break
    else:
        index+=1
        if index>=size:
            index=0
            size+=1
        mat[next[1]][next[2]]=0
        dist=next[0]
        queue = collections.deque([[next[1], next[2], size, next[0]]])
        # bfs(collections.queue([next[1], next[1], size, dist]))
if next==-1:
    print(dist)
else:
    print(next[0])