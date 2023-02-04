n = int(input())
target = int(input())
num = n*n

mat = [[0]*n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

nx, ny = 0, 0
mat[nx][ny] = num
num-=1
index = 0
while (num>1):

    for i in range(4):
        nx, ny = nx + dx[i], ny + dy[i]
        while index <= nx < n and index <= ny < n:
            if mat[nx][ny]==0:
                mat[nx][ny] = num
                num-=1
                nx, ny = nx + dx[i], ny + dy[i]
            else:
                nx +=1
                ny +=1
                mat[nx][ny]=num
                num-=1
                n-=1
                index+=1
                break
        if i==3:
            break
        else:
            nx, ny = nx - dx[i], ny - dy[i]
        # continue

for i in mat:
    print(" ".join(map(str, i)))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]==target:
            print(f'{i+1} {j+1}')
            