sen1 = input()
sen2 = input()

mat = [[0 for _ in range(len(sen1))] for _ in range(len(sen2))]

if sen1[0]==sen2[0]:
    mat[0][0]=1

for i in range(1, len(sen1)):
    if sen1[i]==sen2[0]:
        mat[0][i] = 1
    else:
        mat[0][i] = mat[0][i-1]
for i in range(1, len(sen2)):
    if sen2[i]==sen1[0]:
        mat[i][0] =1
    else:
        mat[i][0] = mat[i-1][0]


for i in range(1, len(sen1)):
    for j in range(1, len(sen2)):
        if sen1[i]==sen2[j]:
            mat[j][i] = mat[j-1][i-1]+1
        else:
            mat[j][i] = max(mat[j-1][i], mat[j][i-1])

# for m in mat:
    # print(m)
print(mat[-1][-1])