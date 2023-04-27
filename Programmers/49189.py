from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    length = len(edge)
    for i in range(length):
        edge.append([edge[i][1], edge[i][0]])
    dictv = defaultdict(lambda :0)
    mat=[[]for _ in range(n+1)]
    for i in range(len(edge)):
        mat[edge[i][0]].append(edge[i][1])
    dictv[1]=1
    
    queue = deque([1])    
    while queue:
        node = queue.popleft()
        for i in mat[node]:
            if (dictv[i]==0):
                queue.append(i)
                dictv[i] = dictv[node]+1
    temp=0
    for i in list(dictv.values()):
        if i>temp:
            temp=i
            answer=1
        elif i==temp:
            answer+=1
    
    
    return answer
