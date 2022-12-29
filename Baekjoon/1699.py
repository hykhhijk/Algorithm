n = int(input())
index = int(n**0.5)+1
powers = [i*i for i in range(1, index)]
dp = [i for i in range(n+1)]

for i in powers:
    dp[i] = 1
    
for i in range(len(dp)):
    for power in powers:
        if i > power:
            if dp[i-power]+1 < dp[i]:
                dp[i] = dp[i-power]+1

print(dp[n])