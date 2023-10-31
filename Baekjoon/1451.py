import sys

n, m = map(int, input().split())

mat = []
for _ in range(n):
    temp_input = sys.stdin.readline().strip()
    mat.append([int(i) for i in temp_input])
    result = 0

for row in range(n):
    for col in range(m):
        space1=[0, 0, 0]
        space2=[0, 0, 0]
        space3=[0, 0, 0]
        space4=[0, 0, 0]

        total = 1
        for i in range(n):
            if i <= row:
                space1[0] +=sum(mat[i][:col])
                space1[1] += sum(mat[i][col:])
            else:
                space1[2] +=sum(mat[i])
        if result < space1[0] * space1[1] * space1[2]:
            result=space1[0] * space1[1] * space1[2]

        for i in range(n):
            if i <= row:
                space2[0] +=sum(mat[i])
            else:
                space2[1] += sum(mat[i][:col])
                space2[2] += sum(mat[i][col:])
        if result < space2[0] * space2[1] * space2[2]:
                result =space2[0] * space2[1] * space2[2]

        for i in range(n):
            if i <= row:
                space3[0] +=sum(mat[i][:col])
                space3[1] += sum(mat[i][col:])
            else:
                space3[0] +=sum(mat[i][:col])
                space3[2] += sum(mat[i][col:])
        if result < space3[0] * space3[1] * space3[2]:
                result =space3[0] * space3[1] * space3[2]

        for i in range(n):
            if i <= row:
                space4[0] +=sum(mat[i][:col])
                space4[1] += sum(mat[i][col:])
            else:
                space4[2] +=sum(mat[i][:col])
                space4[1] +=sum(mat[i][col:])
        if result < space4[0] * space4[1] * space4[2]:
                result =space4[0] * space4[1] * space4[2]
for i in range(n):
    for j in range(i, n):
        space5=[0, 0, 0]
        for row in range(n):
            if row < i:
                space5[0] += sum(mat[row])
            elif i <= row < j:
                space5[1] += sum(mat[row])
            else:
                space5[2] += sum(mat[row])
        if result < space5[0] * space5[1] * space5[2]:
                result =space5[0] * space5[1] * space5[2]
for i in range(m):
    for j in range(i, m):
        space6=[0, 0, 0]
        for row in range(n):
            space6[0] += sum(mat[row][:i])
            space6[1] += sum(mat[row][i:j])
            space6[2] += sum(mat[row][j:])
        if result < space6[0] * space6[1] * space6[2]:
            result=space6[0] * space6[1] * space6[2]
print(result)