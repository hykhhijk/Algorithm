import sys

n = int(input())
time_list=[]
value_list=[]
for _ in range(n):
    time, value = map(int, sys.stdin.readline().split())
    time_list.append(time)
    value_list.append(value)
dp = [0 for _ in range(n+1)]

for i in range(n):
    time = time_list[i]
    if i > 1:
        dp[i] = max(dp[i-1], dp[i])
    if i + time > n:
        continue
    dp[time+i] = max(dp[time+i], dp[i] + value_list[i])
    

print(max(dp))