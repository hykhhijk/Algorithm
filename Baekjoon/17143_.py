import sys

R, C, M  = map(int, input().split())
sharks = []
mat = [[0]*(C+1) for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    mat[r][c] = [s, d, z]
result = 0

def search(col):
    global result
    for i in range(1, R+1):
        if mat[i][col]!=0:
            result+=mat[i][col][2]
            mat[i][col] = 0
            break

def move():
    sharcks = []
    for i in range(1, r+1):
        for j in range(1, c+1):
            if mat[i][j]!=0:
                s, d, z = mat[i][j]
                if d==1:
                    x, y= i-s, y

                if x < 1 or x > R or y <1 or y>C:
                    if d%2==0:
                        d -=1
                    else:
                        d+=1
for i in range(1, C+1):
    search(i)
    move()
    print(result)
