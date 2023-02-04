n = int(input())

num_list = [0 for _ in range(n+1)]

num_list[0] = 1
num_list[1] = 1

for i in range(2, n+1):
    num_list[i] = num_list[i-1] + num_list[i-2]

print(num_list[n] % 10007)