import sys
import math
from collections import deque


mat = [False for _ in range(10000)] #False = 소수
mat[0]=True
mat[1]=True


for i in range(2,int(math.sqrt(len(mat)))+1):
    if mat[i]==False:
        index = i*2
        while index < 10000:
            mat[index]=True
            index += i

t = int(input())
for i in range(t):
    num1, num2 = map(int, sys.stdin.readline().split())
    visited = [math.inf for _ in range(10000)]
    visited[num1] = 0
    queue = deque([num1])
    while queue:
        num = queue.popleft()
        for i in range(4):
            chars = [c for c in str(num)]
            for j in range(0, 10):
                chars[i] = str(j)
                temp = int("".join(chars))
                if temp < 1000:
                    continue
                if mat[temp] == True:
                    continue
                if visited[num]+1 <= visited[temp]:     #bfs + 겹치는 케이스 없음 -> num2를 처음 도달했을때가 최적이므로 고려하지 않고 그냥 bfs의 visited개념 사용하면됨
                    visited[temp] = visited[num] + 1
                    queue.append(temp)

    print(visited[num2])
                