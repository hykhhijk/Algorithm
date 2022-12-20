n = int(input())
num_list = list(map(int, input().split()))
dp_list = [1 for _ in range(n+1)]

for i in range(len(num_list)):
    for j in range(i):
        if num_list[i] < num_list[j]:
            dp_list[i] = max(dp_list[j]+1, dp_list[i])

print(max(dp_list))