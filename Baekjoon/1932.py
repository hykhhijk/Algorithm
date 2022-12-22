import copy

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
dp_list = copy.deepcopy(triangle)
# dp_list[1][0] += triangle[0][0] 
# dp_list[1][1] += triangle[0][0] 

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp_list[i][j] += dp_list[i-1][j]
        elif j==i:
            dp_list[i][j] += dp_list[i-1][j-1]
        else:
            dp_list[i][j] += max(dp_list[i-1][j],dp_list[i-1][j-1])

print(max(dp_list.pop()))
