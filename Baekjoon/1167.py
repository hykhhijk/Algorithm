import sys
from collections import deque
import math

n = int(input())
mat = [[]for _ in range(n+1)]

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(nums)-1, 2):
        if nums[i]==-1:
            break
        else:
            mat[nums[0]].append([nums[i], nums[i+1]])
visited = [False for _ in range(n+1)]
visited[0] = True
visited[1] = 1

queue = deque([1])
while queue:
    index = queue.popleft()
    for num in mat[index]:
        node, dist = num
        if visited[node] == False:
            visited[node] = visited[index] + dist
            queue.append(node)
max_index = -1
max_value = 0
for i in range(len(visited)):
    if visited[i] > max_value:
        max_index = i
        max_value = visited[i]

visited = [False for _ in range(n+1)]
visited[0] = True
visited[max_index] = 1

queue = deque([max_index])
while queue:
    index = queue.popleft()
    for num in mat[index]:
        node, dist = num
        if visited[node] == False:
            visited[node] = visited[index] + dist
            queue.append(node)
print(max(visited)-1)