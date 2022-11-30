import sys

t = int(input())

num_list=[]
num_list = [int(sys.stdin.readline())for _ in range(t)]

max_index = 1000000
prime_mat = [False, False] + [True for _ in range(max_index-1)]
for i in range(2, int(max_index**0.5 + 1)):
    if prime_mat[i]==True:
        for j in range(i*2, max_index, i):
            prime_mat[j] = False

for i in num_list:
    result=0
    for j in range((i//2)+1):
        if prime_mat[j]==True and prime_mat[i-j]==True:
            result+=1
    print(result)