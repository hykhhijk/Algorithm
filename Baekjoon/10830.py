import copy

N, B = map(int, input().split())

mat=[]
for _ in range(N):
    mat.append(list(map(int, input().split())))

result_mat=copy.deepcopy(mat)

while B>1:
    if B%2==0:
        before = copy.deepcopy(result_mat)
        for i in range(N):
            for j in range(N):
                result_mat[i][j] = sum([before[i][index] * before[index][j]for index in range(N)])%1000
        B=B//2
    else:
        before = copy.deepcopy(result_mat)
        for i in range(N):
            for j in range(N):
                result_mat[i][j] = sum([before[i][index] * mat[index][j]for index in range(N)])%1000
        B-=1
    for i in result_mat:
        print(" ".join(map(str,i)))
    print(B)

for i in result_mat:
    print(" ".join(map(str,i)))
