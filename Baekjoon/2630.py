import sys
n = int(input())
m = n//2
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

white=0
blue=0
def recursive(row, col, m):
    global white
    global blue
    if m==0:
        if mat[row][col]==0:
            white +=1
        else:
            blue+=1
        return
    if mat[row][col] == mat[row-1][col] == mat[row][col-1] == mat[row-1][col-1]:
        if mat[row][col]==0:
            white +=1
        else:
            blue+=1
    else:
        m=m//2
        if m==0:
            recursive(row - 1, col - 1, 0)
            recursive(row, col - 1, 0)
            recursive(row - 1, col, 0)
            recursive(row, col, 0)
        else:
            recursive(row + m, col + m, m)
            recursive(row + m, col - m, m)
            recursive(row - m, col + m, m)
            recursive(row - m, col - m, m)

recursive(m, m, m)
print(white)

print(blue)
    