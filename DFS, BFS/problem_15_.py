from collections import deque

from numpy import empty

n, m, k, x = map(int, (input().split()))

mat = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    mat[start].append(end)

distance = [-1] * (n+1)
distance[x] = 0

queue = deque()
def bfs(x):
    queue.append(x)
    while queue:

        x = queue.popleft()
        for i in range(len(mat[x])):
            if distance[mat[x][i]] == -1:
                queue.append(mat[x][i])
                distance[mat[x][i]] = distance[x]+1
                if distance[mat[x][i]] == k+1:
                    return
bfs(x)
result = []
for i in range(n+1):
    if distance[i]==k:
        result.append(i)
result.sort()
if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i])