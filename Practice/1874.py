import sys
from collections import deque

n = int(input())
targets=deque([])
for _ in range(n):
    targets.append(int(sys.stdin.readline().strip()))

right = deque([i+1 for i in range(n)])
left = []
result = []
while targets:
    target = targets.popleft()
    while right and right[0] <= target:
        left.append(right.popleft())
        result.append("+")
    if left[-1] == target:
        left.pop()
        # right.appendleft(left.pop())
        result.append("-")
    # right.popleft()
    # print(left, right)

if right or left:
    print("NO")
else:
    for r in result:
        print(r)

