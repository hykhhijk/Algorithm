import sys

n, k = map(int, input().split())
coins=[]
dp = [0 for _ in range(k+1)]
for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))
# coins.sort()
dp[0] = 1

for i in range(len(dp)):
    for j in range(len(coins)):
        if i - coins[j] >= 0:
            dp[i] += dp[i - coins[j]]

print(dp)