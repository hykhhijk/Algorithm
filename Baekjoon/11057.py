n = int(input())

num_list = [[0]*10 for _ in range(n)]
num_list[0] = [1,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
    for j in range(10):
        # if j==0:
        #     for k in range(1, 10):
        #         num_list[i][j] += num_list[i-1][k]
        # else:
        for k in range(j, 10):
            num_list[i][j] += num_list[i-1][k]


print(sum(num_list[n-1])%10007)