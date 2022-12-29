import sys

n = int(input())
num_list=[]
for _ in range(n):
    num_list.append(list(map(int, sys.stdin.readline().split())))
dp = [0 for _ in range(n+1)]

for i in range(len(num_list)):
    dp[i] = max(dp[i], dp[i-1])
    if i + num_list[i][0] < n+1:
        dp[i+num_list[i][0]] = max(dp[i]+num_list[i][1], dp[i+num_list[i][0]])
print(max(dp))