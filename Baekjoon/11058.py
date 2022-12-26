n = int(input())
dp = [0 for _ in range(n+1)]
temp = 0
mul = False
i=0

while i < n:
    if mul == False:
        if i+3 < n:
            dp[i+2] = max(dp[i-1]+3, dp[i-1]*2)
            mul = True
            temp = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
    else:
        if i+3 < n:
            dp[i+2] = max(dp[i-1]+(3*temp), dp[i-1]*2)
            mul = True
            temp = dp[i-1]
        else:
            dp[i] = dp[i-1] + temp
    i+=1

print(dp[n-1])