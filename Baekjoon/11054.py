n = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(n)]
dp_decrease = [1 for _ in range(n)]

for i in range(1, len(seq)):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[j]+1, dp[i])

for i in range(len(seq), -1, -1):
    for j in range(i, len(seq)):
        if seq[j] < seq[i]:
            dp_decrease[i] = max(dp_decrease[j]+1, dp_decrease[i])

for i in range(len(dp)):
    dp[i] = dp[i] + dp_decrease[i]

print(max(dp)-1)