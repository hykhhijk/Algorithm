import sys

n = int(input())

graph = [[] for _ in range(200001)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x, y = x+100000, y+100000
    graph[x].append(y)

for i in range(len(graph)):
    if len(graph[i]) != 0:
        graph[i].sort()
        for j in graph[i]:
            print(i-100000, j-100000)