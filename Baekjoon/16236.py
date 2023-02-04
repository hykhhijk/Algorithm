import sys

N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))


size = 2
feed = []
wall = []
for row in range(N):
    for col in range(N):
        if  mat[row][col]!=0 and mat[row][col] < size:
            feed.append([row, col, mat[row][col]])
        elif mat[row][col] > size:
            wall.append([row, col])
            
