n = int(input())
num_list = list(map(int, input().split()))
dp_list = num_list.copy()
# dp_list = [0 for _ in range(n+1)]
# dp_list[0] = num_list[0]

for i in range(len(num_list)):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp_list[i] = max(dp_list[i], dp_list[j]+num_list[i])
# print(dp_list)
print(max(dp_list))
