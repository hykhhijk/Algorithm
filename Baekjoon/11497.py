import sys
import collections

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    sticks = list(map(int, sys.stdin.readline().split()))
    sticks.sort()
    q = collections.deque([])
    for i in range(len(sticks)):
        if i%2==1:
            q.append(sticks.pop())
        else:
            q.appendleft(sticks.pop())
    q = list(q)
    index = 0
    for i in range(1, len(q)):
        if index < abs(q[i-1] - q[i]):
            index = abs(q[i-1] - q[i])
    print(index)