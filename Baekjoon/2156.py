import sys

n = int(input())
wines = [0 for _ in range(10001)]
for i in range(n):
    wines[i] = int(sys.stdin.readline().strip())
dp = [0 for _ in range(10001)]
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
# dp[2] = max((wines[0] + wines[2]), (wines[1] + wines[2]))

for i in range(2, n):
    dp[i] = max((dp[i-2] + wines[i]), (dp[i-3] + wines[i-1] + wines[i]), (dp[i-1]))

print(max(dp))