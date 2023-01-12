import sys
sys.setrecursionlimit(10**5)
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
visit = [[False]*n for _ in range(n)]

heights = set([])
for i in range(len(mat)):
    for j in range(len(mat[i])):
        heights.add(mat[i][j])

def dfs(row, col, height):
    if row < 0 or row >= n or col < 0 or col >=n:
        return 0
    elif mat[row][col] > height and visit[row][col]==False:
        visit[row][col] = True
        dfs(row+1, col, height)
        dfs(row-1, col, height)
        dfs(row, col+1, height)
        dfs(row, col-1, height)
        return 1
    else:
        return 0

result_list=[]
for height in heights:
    result=0
    visit = [[False]*n for _ in range(n)]
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            result += dfs(row, col, height)
    result_list.append(result)
result = max(result_list)
if result==0:
    print(1)
else:
    print(result)