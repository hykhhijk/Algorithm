n = int(input())

mat =[]
count=0
mat_list=[]
temp = 0
for _ in range(n):
    mat.append(list(map(int, input())))

visited = [[False]*(n+1) for _ in range(n+1)]

def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= n:
        return False
    if mat[row][col] == 0:
        return False
    elif mat[row][col] == 1 and visited[row][col] == False:
        visited[row][col] = True
        global temp
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
        temp += 1
        return True    
    
for i in range(n):
    for j in range(n):
        if dfs(i, j) ==True:
            count += 1
            mat_list.append(temp)
            temp = 0
            
mat_list.sort()

print(count)
for i in range(len(mat_list)):
    print(mat_list[i])