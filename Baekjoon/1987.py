import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
r,c = map(int, input().split())
mat = []

for _ in range(r):
    # mat.append(list(map(int, sys.stdin.readline().split())))
    mat.append(list(sys.stdin.readline().strip()))

# strings = [[[] for _ in range(c)]for _ in range(r)]
# strings[0][0] = [mat[0][0]]

queue = set([(0, 0, mat[0][0])])

def bfs():
    answer = 1
    while queue:
        x, y, index = queue.pop()
        # if answer < len(strings[x][y][index]):
            # answer = len(strings[x][y][index])
        for i in range(4):
            nx, ny = x+ dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or mat[nx][ny] in index:
                continue
            else:
                queue.add((nx, ny, index + mat[nx][ny]))
                answer=max(answer,len(index)+1)

                # path = strings[x][y][index]         #path는 이때까지 걸쳐온 문자열
                # for p in path:
                    # if p==mat[nx][ny]:    
                        # break                
                # else:
                    # strings[nx][ny].append(path+mat[nx][ny])
                    # queue.append([nx,ny,len(strings[nx][ny])-1])
    return answer


print(bfs())
        