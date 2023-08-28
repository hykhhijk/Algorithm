import sys

def check(x, y, n):
    global result
    if n==0:
        result.append(mat[x][y])
        return 
    value = 0
    for i in range(y, y+n):
        for j in range(x, x+n):
            value += mat[i][j]
    if value != n**2 and value !=0:
        result.append("(")
        check(x, y, n//2)
        check(x+n//2, y, n//2)
        check(x, y+n//2, n//2)
        check(x+n//2, y+n//2, n//2)
        result.append(")")
    else:
        if value ==0:
            result.append("0")
        else:
            result.append("1")



n = int(input())
mat = []
result = []
for _ in range(n):
    temp = list(sys.stdin.readline().strip())
    mat.append([int(i) for i in temp])
    

check(0, 0, n)
print("".join(result))

