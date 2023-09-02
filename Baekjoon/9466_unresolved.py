import sys
sys.setrecursionlimit(10**6)

def bfs(index):
    global result
    visited = [False for _ in range(len(nums)+1)]
    graph = [index]
    while True:
        visited[index] = True
        next = nums[index]
        if nums[next]==0:
            for i in graph:
                nums[i]=0
            result += len(graph)
            return
        elif visited[next]==True:
            for i in range(len(graph)):
                nums[graph[i]]=0
                if graph[i]==next:
                    result += (len(graph[:i]))
                nums[index]=0
            return                    
        graph.append(next)
        index = nums[next]


result = 0
t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    nums = [0] + nums
    result = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            temp = bfs(i)
            if temp==1:
                break
    print(result)