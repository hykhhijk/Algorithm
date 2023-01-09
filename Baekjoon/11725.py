import sys
import collections

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
visited[1] = 1
queue = collections.deque([])
for i in range(n-1):
    temp = list(map(int, sys.stdin.readline().split()))
    tree[temp[0]].append(temp[1])
    tree[temp[1]].append(temp[0])
queue.append(1)
while queue:
    index = queue.popleft()
    for i in range(len(tree[index])):
        if visited[tree[index][i]] == 0:
            visited[tree[index][i]] = index
            queue.append(tree[index][i])

for i in range(2, len(visited)):
    print(visited[i])

