import sys
from collections import deque
import math

indexes = [[1, 2],[0, 2],[0, 1]]

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
dp = [[math.inf, math.inf, math.inf] for _ in range(n)]
dp[0] = mat[0]

for i in range(1, len(dp)):
    for j in range(3):
        dp[i][j] = min(mat[i][j] + dp[i-1][indexes[j][0]], mat[i][j] + dp[i-1][indexes[j][1]])

print(min(dp[-1]))