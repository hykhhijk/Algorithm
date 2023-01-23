import sys
import collections

N = int(input())
mat = [[0]*(N+1) for _ in range(N+1)]
K = int(input())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    mat[r][c] = 1
L = int(input())
command = []
for _ in range(L):
    command.append(list(sys.stdin.readline().split()))
command = collections.deque(command)

snake = collections.deque([[1, 1]])
rot, degree = command.popleft()
dir = 0
time = 0
while True:
    r, c = snake[-1][0], snake[-1][1]
    if r < 1 or r > N or c < 1 or c > N :
        break
    if dir==0:
        next_r, next_c = r, c+1
    elif dir==1:
        next_r, next_c = r+1, c
    elif dir==2:
        next_r, next_c = r, c-1
    elif dir==3:
        next_r, next_c = r-1, c
    time +=1
    if [next_r, next_c] in snake:
        break
    if time==int(rot):
        if degree=="L":
            dir-=1
        else:
            dir+=1
        dir = dir%4
        if command:
            rot, degree = command.popleft()
        else:
            pass
    if mat[r][c]==0:
        snake.popleft()
        snake.append([next_r, next_c])    
    else:
        mat[r][c]=0
        snake.append([next_r, next_c])

print(time)