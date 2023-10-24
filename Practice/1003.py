t = int(input())

nums = []
for _ in range(t):
    nums.append(int(input()))
mat = [[0,0] for _ in range(41)]

mat[0] = [1, 0]
mat[1] = [0, 1]

for i in range(2, 41):
    mat[i][0] = mat[i-1][0] + mat[i-2][0]
    mat[i][1] = mat[i-1][1] + mat[i-2][1]

for n in nums:
    print(" ".join(map(str, mat[n])))

