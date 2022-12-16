import sys

mat = [0 for i in range(10002)]

n = int(input())

for _ in range(n):
    mat[int(sys.stdin.readline().strip())] +=1

for i in range(len(mat)):
    while mat[i] > 0:
        print(i)
        mat[i]-=1