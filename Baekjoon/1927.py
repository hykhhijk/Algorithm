import heapq
import sys

n = int(input())
num_list=[]

for _ in range(n):
    command = int(sys.stdin.readline().strip())
    if command==0:
        if num_list:
            print(heapq.heappop(num_list))
        else:
            print(0)
    else:
        heapq.heappush(num_list, command)
