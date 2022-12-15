import heapq
import sys

n = int(input())
num_list=[]
small_list=[]

for _ in range(n):
    command = int(sys.stdin.readline().strip())
    # print(f"command: {command}")
    if command==0:
        if num_list:
            if small_list and small_list[0] == num_list[0]:
                result = heapq.heappop(num_list)
                print(-result)
                heapq.heappop(small_list)
            else:
                print(heapq.heappop(num_list))
        else:
            print(0)
    else:
        if command < 0:
            heapq.heappush(num_list, -command)
            heapq.heappush(small_list, -command)
        else:
            heapq.heappush(num_list, command)
    # print(num_list)
    # print(small_list)