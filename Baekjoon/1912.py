n = int(input())
num_list = list(map(int, input().split()))
# dp_list = [0 for _ in range(n+1)]
# dp_list[0] = num_list[0]
dp_list = num_list.copy()

for i in range(1, len(num_list)):
    if dp_list[i]==num_list[i]:
        dp_list[i] = max(dp_list[i-1] + num_list[i], num_list[i])

print(max(dp_list))
