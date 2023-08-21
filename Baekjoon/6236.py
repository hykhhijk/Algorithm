import sys
from copy import deepcopy

def check(mid):
    result = 1
    temp = deepcopy(mid)
    for i in range(len(costs)):
        if costs[i] > temp:
            result +=1
            temp = deepcopy(mid)
        temp -= costs[i]
    return result

n, m = map(int, input().split())

costs = []
for _ in range(n):
    costs.append(int(sys.stdin.readline().strip()))

start, end = 0, 10000000000000000000            #값을 지정하지 못한 부분에서 name error? -> 아마 answer가 아예 초기화 되지 못하면서 생기는듯
max_cost = max(costs)
while start <= end:
    mid = (start + end)//2
    index = check(mid)
    if  max_cost > mid or index > m:
        start = mid +1
    else:
        answer = mid
        end = mid-1

print(answer)