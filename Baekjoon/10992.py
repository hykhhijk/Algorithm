n = int(input())

mat = [[" " for _ in range((2*n)-1)] for _ in range(n)]
index = n
mat[0][index-1] = "*"
for j in range(index, len(mat[0])):
        mat[0].pop()
index += 1

for i in range(1, n):
    mat[i][index-1] = "*"
    mat[i][index-1-(i*2)]="*"
    for j in range(index, len(mat[i])):
        mat[i].pop()
    index+=1
for i in range(len(mat[-1])):
    mat[-1][i] = "*"

for i in mat:
    print("".join(i))