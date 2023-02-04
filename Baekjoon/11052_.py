n = int(input())

prices = list(map(int, input().split()))
prices.insert(0, 0)
dp = [0 for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(i+1):
        dp[i] = max(dp[i], prices[i-j] + dp[j])

print(dp.pop())
