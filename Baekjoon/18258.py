import collections
import sys

deque = collections.deque()

n = int(input())
for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        deque.append(command[1])
    elif command[0] == "pop":
        if deque:
            temp = deque.popleft()
            print(temp)
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
