import sys


def check(x, y, n):
    global result
    if n==1:
        result[mat[x][y]] += 1
        return
    first = mat[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if mat[i][j] != first:
                check(x, y, n//3)
                check(x, y+n//3, n//3)
                check(x, y+2*n//3, n//3)
                check(x+n//3, y, n//3)
                check(x+n//3, y+n//3, n//3)
                check(x+n//3, y+2*n//3, n//3)
                check(x+2*n//3, y, n//3)
                check(x+2*n//3, y+n//3, n//3)
                check(x+2*n//3, y+2*n//3, n//3)
                return
    result[mat[x][y]] += 1




n = int(input())
mat = []
result = [0, 0, 0]
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

check(0, 0, n)

print(result[-1])
print(result[0])
print(result[1])

