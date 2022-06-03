from collections import deque

m, n = map(int, input().split())

mat=[]
for i in range(n):
    mat.append(list(map(int, input().split())))
x_move = [1, -1, 0, 0]
y_move = [0, 0, 1, -1]


def tomato(location):
    queue=deque()
    for i in location:
        queue.append([i[0], i[1]])
        while queue:
            x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + x_move[i], y + y_move[i]
            if next_x < 0 or next_x >m-1 or next_y < 0 or next_y > n-1:
                print(next_x, next_y)
                continue
            elif mat[next_x][next_y] == -1:
                continue
            elif mat[next_x][next_y] == 0:
                mat[next_x][next_y] = mat[x][y]+1
                queue.append([next_x, next_y])
    return 0
        
ripen=[]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]==1:
            ripen.append([j, i])


tomato(ripen) 
result=0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] > result:
            result=mat[i][j]   
print(mat)
print(result)