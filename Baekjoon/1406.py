import sys

left = list(input())
right = []
n = int(input())
# location = len(text)        #0은 왼쪽에 수가 없음 n은 오른쪽에 수가 없음

for i in range(n):
    command = list(sys.stdin.readline().split())
    if command[0]=="L":
        if not left:
            continue
        else:
            right.append(left.pop())
    elif command[0]=="D":
        if not right:
            continue
        else:
            left.append(right.pop())
    elif command[0]=="B":
        if not left:
            continue
        else:
            left.pop()
    elif command[0]=="P":
            left.append(command[1])
right.reverse()
print("".join(left+right))