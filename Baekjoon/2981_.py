import sys

n = int(input())
num_list=[]
for i in range(n):
    num_list.append(int(sys.stdin.readline().strip()))

num_list.sort()

num_list = [num_list[i+1]-num_list[i] for i in range(len(num_list)-1)]
num_list = list(set(num_list))
def n_and_m(num, div):
    while True:
        temp = num % div
        if temp==0:
            return div
        else:
            num = div
            div = temp

gcd = num_list[0]
for i in range(1, len(num_list)):
    gcd = n_and_m(num_list[i], gcd)
result_list=[]
for i in range(2, int(gcd**0.5+1)):
    if gcd % i ==0:
        result_list.append(i)
        result_list.append(int(gcd/i))
result_list = list(set(result_list))
result_list.sort()
for i in result_list:
    print(i, end=" ")
print(gcd)
