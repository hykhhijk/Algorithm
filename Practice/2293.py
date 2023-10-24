n, k = map(int,input().split())
values = []
for _ in range(n):
    values.append(int(input()))

mat = [0 for _ in range(k+1)]
mat[0]=1

for i in range(1, len(mat)):
    if i % values[0]==0:
        mat[i]=1

for val in values[1:]:
    for col in range(val, len(mat)):
        mat[col] = mat[col]  + mat[col-val]
print(mat[-1])  