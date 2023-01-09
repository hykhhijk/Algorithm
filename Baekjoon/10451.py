import sys

t = int(input())

for _ in range(t):
    n = int(input())
    edges = [0 for _ in range(n+1)]
    nodes = list(map(int, sys.stdin.readline().split()))
    for i in range(len(nodes)):
        edges[i+1] = nodes[i]
    visited = [False] * (n+1)
    count=0
    for i in range(len(edges)):
        if visited[edges[i]]==False:
            count+=1
            index = edges[i]
            while visited[i]==False:
                visited[index] = True
                index = edges[index]

    print(count - 1)