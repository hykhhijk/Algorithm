import sys

n = int(input())

num_list=[]
for _ in range(n):
    num_list.append(int(sys.stdin.readline().strip()))
num_list.sort()
for i in num_list:
    print(i)