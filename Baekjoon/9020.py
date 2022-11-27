import sys

T = int(input())

num_list=[]
for i in range(T):
    num_list.append(int(sys.stdin.readline().rstrip()))

mat_target = max(num_list)
prime_mat = [True for _ in range(mat_target+1)]

for i in range(2, int(mat_target**0.5)+1):
    if prime_mat[i]==True:
        temp=2
        while i*temp < mat_target:
            prime_mat[i*temp]=False
            temp+=1

for i in num_list:
    div_num = int(i/2)
    to_zero = div_num
    to_max = div_num
    while True:
        if prime_mat[to_zero]==True and prime_mat[to_max] ==True:
            print(to_zero, to_max)
            break
        else:
            to_zero-=1
            to_max+=1
        