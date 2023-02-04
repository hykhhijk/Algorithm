import sys

n, k = map(int, input().split())
coins=[]
for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))
dp = [10001]*(k+1)
coins.sort()

for i in range(len(coins)):
    for j in range(len(dp)):
        if j % coins[i]==0:
            dp[j] = min(j//coins[i], dp[j])
        else:
            if j - coins[i] > 0:
                # for k in range(i):
                dp[j] = min(dp[j-coins[i]]+1, dp[j])
                # for k in (j, 0, -coins[i]):
                    # dp[i][j] = min(dp[i][k]+1, dp[i-1][k]+1)
result = dp[k]
if result>=10001:
    print(-1)
else:
    print(result)