import sys

n, k = map(int, input().split())
w_list = []
v_list = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    w_list.append(w)
    v_list.append(v)
    
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(len(w_list)):
    for j in range(len(dp[i])):
        if j >= w_list[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_list[i]] + v_list[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][k])