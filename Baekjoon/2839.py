from cmath import inf


num = int(input())

mat = [inf]*5001

for i in range(3, num+1):
    if i==3 or i==5:
        mat[i]=1
    else:
        mat[i] = min(mat[i-3]+1, mat[i-5]+1)

if mat[num]==inf:
    print(-1)
else:
    print(mat[num])