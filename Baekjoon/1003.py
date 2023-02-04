import sys

zero_list= [0 for _ in range(41)]
one_list= [0 for _ in range(41)]

n = int(input())
zero_list[0] += 1
one_list[1] += 1

def fibo(x):
    if x==0:
        return zero_list[0], one_list[0]
    elif x==1:
        return zero_list[1], one_list[1]
    else:
        if zero_list[x]==0 and one_list[x]==0:
            zero_1, one_1 = fibo(x-1)
            zero_2, one_2 = fibo(x-2)
            zero_list[x] = zero_1 + zero_2
            one_list[x] = one_1 + one_2
        return zero_list[x], one_list[x]

fibo(40)
# print(one_list)
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    print(zero_list[num], end=" ")
    print(one_list[num])

