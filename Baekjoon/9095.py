import sys

n = int(input())
num_list = [0 for _ in range(11+1)]
num_list[0] = 1
num_list[1] = 1
num_list[2] = 2
num_list[3] = 4



def dp(x):
    if num_list[x]==0:
        num_list[x] = dp(x-1) + dp(x-2) + dp(x-3)
    return num_list[x]



for _ in range(n):
    num = int(sys.stdin.readline().strip())
    result = dp(num)
    print(result)