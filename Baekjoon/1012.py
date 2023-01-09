import sys
sys.setrecursionlimit(10**6)

def dfs(row, col):
    if mat[row][col]==1 and 0<= row <=n and 0<= col <=m :
        mat[row][col] = 0
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
    else:
        return 0



t = int(input())
for _ in range(t):
    count = 0
    n, m, k = map(int, sys.stdin.readline().split())
    mat = [[0]*(m+1) for _ in range(n+1)]
    for _ in range(k):
        row, col = map(int, sys.stdin.readline().split())
        mat[row][col] = 1
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] == 1:
                count += 1
                dfs(row, col)
    print(count)