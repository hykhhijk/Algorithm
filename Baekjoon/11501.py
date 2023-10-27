import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    prices = list(map(int, sys.stdin.readline().split()))
    value = 0
    answer = 0
    for i in range(len(prices)-1, -1, -1):
        if prices[i] >= value:
            value = prices[i]
        else:
            answer += (value - prices[i])
    print(answer)
