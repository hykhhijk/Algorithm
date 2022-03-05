
mat = [str(i) for i in range(1, 10001)]
result = [i for i in range(1, 10001)]

for i in range(len(mat)):
    temp = int(mat[i])
    for j in range(len(mat[i])):
        temp += int(mat[i][j])
    if temp in result:
        result.remove(temp)
    else:
        pass

for i in range(len(result)):
    print(result[i])