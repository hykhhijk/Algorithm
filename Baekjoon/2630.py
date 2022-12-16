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
    color = mat[row][col]
    for i in range(row, row+m):
        for j in range(col, col+m):         #m범위 내에 모든 mat을 순회
            if color != mat[i][j]:
                recursive(row, col, m//2)
                recursive(row+m//2, col, m//2)
                recursive(row, col+m//2, m//2)
                recursive(row+m//2, col+m//2, m//2)
                return                      #색깔이 하나라도 다를시 4개 영역으로 나눈뒤 종료
                                #m은 1이되면 같은 영역을 한번 참고하므로 color == mat[i][j] -> 모든 색깔이 추가됨
    if color==0:
        white+=1
    else:
        blue+=1

recursive(0,0, n)
print(white)
print(blue)
    