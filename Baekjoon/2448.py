import sys
sys.setrecursionlimit(10**6)

def star(i, row, col):
    if i==3:
        mat[row][col]="*"
        mat[row+1][col-1] = "*"
        mat[row+1][col+1] = "*"

        mat[row+2][col-2] = "*"
        mat[row+2][col-1] = "*"
        mat[row+2][col] = "*"
        mat[row+2][col+1] = "*"
        mat[row+2][col+2] = "*"
    else:
        i = i//2
        star(i, row, col)
        star(i, row+i, col-i)
        star(i, row+i, col+i)

n = int(input())
center = (n//2)+1

mat = [[" " for _ in range(n//3*5 + (n//3)-1)] for _ in range(n)]

star(n, 0, n-1)

for i in mat:
    print("".join(i))