import sys

n = int(input())

num_list=[]
result=0
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        result+=num
        num_list.append(num)
    else:
        result -= num_list.pop()

print(result)