import sys
import copy

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    line1 = list(map(int, sys.stdin.readline().split()))
    line2 = list(map(int, sys.stdin.readline().split()))
    dp1 = copy.deepcopy(line1)
    dp2 = copy.deepcopy(line2)
    if n >= 2:
        dp1[1] += dp2[0]
        dp2[1] += dp1[0]

    for i in range(2, n):
        dp1[i] += max(dp2[i-1], dp1[i-2], dp2[i-2])
        dp2[i] += max(dp1[i-1], dp1[i-2], dp2[i-2])

    print(max(dp1.pop(), dp2.pop()))