import sys

cursor_left = list(input())
cursor_right= []

n = int(input())

cursor = len(cursor_left)-1
# print(cursor)

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "L":
        if len(cursor_left) == 0:
            continue
        else:
            cursor_right.append(cursor_left.pop())
            cursor-=1
    elif command[0] == "D":
        if len(cursor_right) == 0:
            continue
        else:
            cursor_left.append(cursor_right.pop())
            cursor+=1
    elif command[0] == "B":
        if len(cursor_left)==0:
            continue
        else:
            cursor_left.pop()
    elif command[0] == "P":
        cursor_left.append(command[1])

cursor_right.reverse()
result = cursor_left+cursor_right
for i in result:
    print(i, end="")