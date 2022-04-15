import sys

n = int(input())

mat = [0 for _ in range(10001)]


for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    mat[num] += 1

for num in range(1, 10001):
    if mat[num] != 0:
        while mat[num]:
            print(num)
            mat[num] -= 1
    else:
        continue