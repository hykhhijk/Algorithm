from collections import deque

N, M, T = map(int, input().split())     # N: 원판수, M: 원판 내 원소 수, T: 회전케이스 수
mat = [[]for _ in range(N+1)]
# visited = [[False for _ in range(M)]for _ in range(N+1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    temp = deque(map(int, input().split()))
    mat[i+1] = temp

for i in range(T):
    X, D, K = map(int, input().split())  #X: 회전 원판 번호, D:회전 방향(0은 시계 1은 반시계), K: 회전양
    temp=X
    while X <= N:
        if D==0:
            for _ in range(K):
                mat[X].appendleft(mat[X].pop())
        else:
            for _ in range(K):
                mat[X].append(mat[X].popleft())
        X+=temp
    # print(mat)
    
    check=False
    for i in range(1, len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==0:
                continue
            else:
                queue = deque([[i, j]])
                num = mat[i][j]
                while queue:
                    row, col = queue.popleft()
                    for k in range(4):
                        n_r, n_c = row+dx[k], (col+dy[k])%M
                        if n_r>N or n_r<1:
                            continue
                        if mat[n_r][n_c]==num:
                            mat[i][j]=0
                            mat[n_r][n_c]=0
                            check=True
                            queue.append([n_r, n_c])
    if check==False:
        index=0
        sum_all=0
        for i in range(1, len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]!=0:
                    index+=1
                    sum_all+=mat[i][j]
        avg = sum_all/index
        for i in range(1, len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]!=0:
                    if mat[i][j]>avg:
                        mat[i][j]-=1
                    elif mat[i][j]<avg:
                        mat[i][j]+=1
    # print(mat)
    if sum(map(sum, mat))==0:
        break

print(sum(map(sum, mat)))