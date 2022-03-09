from itertools import combinations

n, m = map(int, input().split())

mat=[]
for i in range(n):
    mat.append(list(map(int, input().split())))

city = []
chicken = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            city.append([i, j])
        elif mat[i][j] == 2:
            chicken.append([i, j])


result=2500
for chick in combinations(chicken, m):
    temp = 0
    for house in city:
        length=2500
        for i in range(m):
            length = min(length, abs(chick[i][0] - house[0]) + abs(chick[i][1] - house[1]))
        temp += length
    result = min(result, temp)

print(result)
# result=[]
# for i in range(len(chicken)):
#     temp=[]
#     for j in range(len(city)):
#         temp.append(abs(chicken[i][0] - city[j][0]) +  abs(chicken[i][1] - city[j][1]))
#     result.append(temp)

# temp=[]
# for i in range(len(result)):
#     temp.append(sum(result[i]))
# for i in range(len(chicken)-m):
#     index = temp.index(max(temp))
#     result.pop(index)
#     temp.remove(max(temp))
# result_ = 0
# for i in range(len(city)):
#     temp=[]
#     for j in range(len(result)):
#         temp.append(result[j][i])
#     result_ += min(temp)
# print(result_)