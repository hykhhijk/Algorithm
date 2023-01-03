import sys

n = int(input())
steps=[]
for i in range(n):
    steps.append(int(sys.stdin.readline().strip()))
dp = [0 for _ in range(n)]
dp[0] = steps[0]
for i in range(1, n):
    if i>2:
        dp[i] = max(steps[i] + steps[i-1] + dp[i-3], steps[i] + dp[i-2])
    elif i==2:
        dp[i] = max(steps[i]+steps[i-1], steps[i]+steps[i-2])
    elif i==1:
        dp[i] = steps[i]+dp[i-1]

print(dp[-1])