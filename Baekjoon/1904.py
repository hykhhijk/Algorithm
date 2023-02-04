n = int(input())

dp = [0 for _ in range(n+1)]
dp[0]=1
dp[1] = 1
for i in range(2, len(dp)):
    dp[i] = dp[i-2] + dp[i-1]
    if dp[i] >= 15746:
        dp[i] %= 15746
print(dp.pop())