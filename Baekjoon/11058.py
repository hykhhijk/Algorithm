n = int(input())

dp = [i for i in range(n+1)]



for i in range(5, n+1):
    dp[i] = max(dp[i-1]+1, dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
    #       dp[i-6]*5 < dp[i-3]*2  ->    5x < 6x이므로 이범위까지는 비교할 필요가 없다

print(dp[-1])