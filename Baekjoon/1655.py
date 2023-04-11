import sys
import collections
import heapq
import copy

n = int(input())
left = []
right = []
num = int(sys.stdin.readline().strip())
left = [-num]
print(-left[0])
for i in range(n-1):
    num = int(sys.stdin.readline().strip())

    if len(left) > len(right):
        heapq.heappush(right,num)          
    else:
        heapq.heappush(left, -num)  #-붙이면 최대힙 됨
    if right and right[0] < -left[0]:
        heapq.heappush(left, -heapq.heappop((right)))
        heapq.heappush(right, -heapq.heappop((left)))

    print(-left[0])