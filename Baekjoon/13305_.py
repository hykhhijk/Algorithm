from math import inf

n = int(input())
edges = list(map(int, input().split()))
nodes = list(map(int, input().split()))




result = 0
while True:
    index = inf
    city = 0
    for i in range(len(nodes)-1, -1, -1):
        if index > nodes[i]:
            index = nodes[i]
            city = i
    result += sum(edges[city:])*index
    nodes = nodes[:city]
    edges = edges[:city]
    if city==0:
        break
print(result)