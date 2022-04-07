from collections import deque

n, m = map(int, input().split())

mat=[]
for i in range(n):
    mat.append(list(map(int, input())))
x_move = [1, -1, 0, 0]
y_move = [0, 0, 1, -1]


def maze(x, y):
    queue=deque()
    queue.append([x, y])
    mat[x][y]=0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + x_move[i], y + y_move[i]
            if next_x < 0 or next_x >n-1 or next_y < 0 or next_y > m-1:
                continue
            elif mat[next_x][next_y] == 0:
                continue
            elif mat[next_x][next_y] == 1:
                mat[next_x][next_y] = mat[x][y]+1
                queue.append([next_x, next_y])
            if next_x == n-1 and next_y == m-1:
                return mat[x][y]+2

result = maze(0, 0)
print(result)