n = int(input())

num_dict = {}
num_set = []
num_list = list(map(int, input().split()))

num_set = list(set(num_list))
num_set.sort()

for i in range(len(num_set)):
    num_dict[num_set[i]] = i

for i in num_list:
    print(num_dict[i], end=" ")