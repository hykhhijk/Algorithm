import sys

N, M = map(int, input().split())
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
mat = []
for _ in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))
command=[]    
for _ in range(M):
    command.append(list(map(int, sys.stdin.readline().split())))
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


for comm in range(len(command)):           #←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
    visited = [[False]*N for _  in range(N)]
    dir, dist = command[comm]

    for i in range(len(cloud)):
        cloud[i][0], cloud[i][1] = (cloud[i][0]+dx[dir-1]*dist)%N, (cloud[i][1] + dy[dir-1]*dist)%N
        mat[cloud[i][0]][cloud[i][1]]+=1
        visited[cloud[i][0]][cloud[i][1]]=True

    for move in [1, 3, 5, 7]:
        for i in range(len(cloud)):
            row, col = cloud[i][0]+dx[move], cloud[i][1]+dy[move]
            if row<0 or row>=N or col<0 or col>=N:
                continue
            else:
                if mat[row][col]>0:
                    mat[cloud[i][0]][cloud[i][1]]+=1
    temp=[]
    # for i in mat:
    #     print(i)
    # print()
    

    for i in range(len(mat)):
        for j in range(len(mat[i])):
                if mat[i][j] >=2 and visited[i][j]==False:
                    temp.append([i, j])
                    mat[i][j]-=2
    cloud = temp


print(sum(map(sum, mat)))