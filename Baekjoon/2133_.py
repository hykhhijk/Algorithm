n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(len(dp)):
    if i==2:
        dp[i] = 3
    elif i==4:
        dp[i] = 11
    elif i>5 and i%2==0:
        dp[i] = dp[i-2]*3
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j]*2
        dp[i] +=2
print(dp[n])