import sys
n = int(input())

stack=[]
def push(num):
    stack.append(num)

def pop():
    if len(stack)==0:
        return -1
    else:
        num = stack.pop()
        return num

def size():
    num = len(stack)
    return num

def empty():
    if len(stack)==0:
        return 1
    else:
        return 0

def top():
    if len(stack)==0:
        return -1
    else:
        return stack[-1]

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0]=="push":
        push(int(command[1]))
    elif command[0]=="size":
        print(size())
    elif command[0]=="pop":
        print(pop())
    elif command[0]=="top":
        print(top())
    elif command[0]=="empty":
        print(empty())
