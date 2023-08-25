import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(x):
    for i in range(len(mat[x])):
        if visited[mat[x][i][0]]==False:
            visited[mat[x][i][0]] = visited[x] + mat[x][i][1]
            dfs(mat[x][i][0])


n = int(input())
nums = [0 for _ in range(n+1)]
mat = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end, value = map(int, sys.stdin.readline().split())
    mat[start].append([end, value])
    mat[end].append([start, value])
    # nums[end] = nums[start] + value

# temp = 0
# for i in range(len(nums)):
    # if nums[i] > temp:
    #     index = i
    #     temp = nums[i]

visited = [False for _ in range(n+1)]
visited[0]=True
visited[1]=1
dfs(1)
index = visited.index(max(visited))

visited = [False for _ in range(n+1)]
visited[0]=True
visited[index]=1
dfs(index)

print(max(visited)-1)