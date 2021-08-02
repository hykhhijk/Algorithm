n, m = map(int, input().split())

mat=[]
for i in range(n):
    mat.append(list(map(int, input())))
result=0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if mat[x][y]==0:
        mat[x][y]=1
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x-1, y)
        return True
    elif mat[x][y]==1:
        return False

for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            result+=1
print(result)


