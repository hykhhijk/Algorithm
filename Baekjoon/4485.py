import sys

while True:
    n = int(input())
    mat = [[] for _ in range(n)]
    for i in range(n):
        mat[i] = (list(map(int, sys.stdin.readline().split())))
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = mat[0][0]
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + mat[0][i]
        dp[i][0] = dp[i-1][0] + mat[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(mat[i][j] + dp[i-1][j], mat[i][j] + dp[i][j-1])
    for i in dp:
        print(i)