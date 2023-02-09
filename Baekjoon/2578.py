import sys

mat = []
for _ in range(5):
    mat.append(list(map(int, input().split())))

command = []
for _ in range(5):
    temp = list(map(int, input().split()))
    for i in temp:
        command.append(i)

check = False
for index in command:
    result = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == index:
                mat[i][j]=0
                check = True
                break
        if check==True:
            check=False
            break
    if mat[0][0]==0 and mat[1][1]==0 and mat[2][2]==0 and mat[3][3]==0 and mat[4][4]==0:
            result+=1
    if mat[0][4]==0 and mat[1][3]==0 and mat[2][2]==0 and mat[3][1]==0 and mat[4][0]==0:
        result+=1
    for k in range(len(mat)):
        bingo_row = 0
        bingo_col = 0
        for l in range(len(mat[k])):
            if mat[k][l]==0:
                bingo_row+=1
            if mat[l][k]==0:
                bingo_col +=1
        if bingo_row==5:
            result+=1
        if bingo_col==5:
            result+=1
        if result>=3:
            print(command.index(index)+1)
            sys.exit()