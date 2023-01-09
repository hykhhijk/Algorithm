import collections

n, m = map(int, input().split())

visited = [0 for _ in range(2000001)]

def bfs(x):
    q = collections.deque([x])
    while q:
        index = q.popleft()
        if index==m:
            return visited[m]
        else:
            for i in (index-1, index+1, index*2):
                if not visited[i] and 0 <= i < 100001:
                    visited[i] = visited[index]+1
                    q.append(i)
print(bfs(n))
# print(visited)