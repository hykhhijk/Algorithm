from collections import deque
n, m, k, x = map(int, input().split())

mat = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    mat[start][end] = 1
    mat[end][start] = 1
visited=[False for _ in range(n+1)]

def bfs(start):
    queue=deque()
    queue.append(start)
    while queue:
        city = queue.popleft()
        visited[city]=True
        for i in range(len(mat[city])):
            if mat[city][i]!=0 and visited[i]==False:
                queue.append(i)
                for j in range(len(mat[i])):
                    if mat[i][j]==1:
                        mat[i][j] = mat[city][i] +1

bfs(x)
def result():
    for i in range(len(mat)):
        if k+1 in mat[i]:
            print(i)
            return True
    return False

result = result()
if result == False:
    print(-1)
        
