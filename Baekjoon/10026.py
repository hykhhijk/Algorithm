import sys
sys.setrecursionlimit(10**5)

n = int(input())
mat=[]
for i in range(n):
    mat.append(list(sys.stdin.readline().strip()))


def  dfs(x, y, color):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    else:
        if mat[x][y]==color and visited[x][y]==False:
            visited[x][y]=True
            dfs(x+1, y, color)
            dfs(x-1, y, color)
            dfs(x, y+1, color)
            dfs(x, y-1, color)
        else:
            return False


count=0
visited = [[False]*(n) for _ in range(n)]
for row in range(len(mat)):
    for col in range(len(mat[row])):
        if visited[row][col]==False:
            count+=1
            dfs(row, col, mat[row][col])
print(count, end=" ")

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=="R":
            mat[i][j]="G"
count=0
visited = [[False]*(n) for _ in range(n)]
for row in range(len(mat)):
    for col in range(len(mat[row])):
        if visited[row][col]==False:
            count+=1
            dfs(row, col, mat[row][col])
print(count)