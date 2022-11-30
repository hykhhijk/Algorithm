import math

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.append(s)

num_list.sort()
min_list = [num_list[i+1] - num_list[i] for i in range(len(num_list)-1)]

gcd=min_list[0]
for i in min_list[1:]:
    gcd = math.gcd(gcd, i)
print(gcd)