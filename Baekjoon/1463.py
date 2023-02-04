num_list = [0 for _ in range(10**6+1)]
num_list[2] = 1
num_list[3] = 1

n = int(input())

if n > 3:
    for i in range(4, n+1):
        num_list[i] = num_list[i-1] + 1
        if i % 2 == 0:
            num_list[i] = min(num_list[i], num_list[i//2] + 1)
        if i % 3 == 0:
            num_list[i] = min(num_list[i], num_list[i//3] + 1)
        
print(num_list[n])
        