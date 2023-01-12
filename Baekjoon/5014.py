import collections

F, S, G, U, D = map(int, input().split())
graph = [i for i in range(S, F+1)]
visit = [0 for _ in range(F+1)]


def bfs(point):
    q = collections.deque([point])
    visit[point] = 1
    while q:
        location = q.popleft()
        next_u = location + U
        next_d = location - D
        if next_u <= 0 or next_u > F:
            pass
        elif visit[next_u]==0:
            visit[next_u]=visit[location]+1
            q.append(next_u)

        if next_d <= 0 or next_d > F:
            pass
        elif visit[next_d]==0:
            visit[next_d]=visit[location]+1
            q.append(next_d)


bfs(S)
result = visit[G]-1
if result==-1:
    print("use the stairs")
else:
    print(result)