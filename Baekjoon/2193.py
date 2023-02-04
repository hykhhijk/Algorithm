n = int(input())

num_list = [0 for _ in range(n+1)]
num_list[1] = 1


if n >= 2:
    num_list[2] = 1
    for i in range(3, n+1):
        num_list[i] = num_list[i-1] + num_list[i-2]

print(num_list[n])            
