from collections import deque
from copy import deepcopy

dir = [[1,2], [0, 2], [0, 1]]
mat = list(map(int, input().split()))
temp = [0,0]
temp.append(mat[-1])
# temp.append(2)
# temp = [0, 0, C의 물용량, 2(C의 인덱스)]
result = [mat]
queue = deque([temp])



#전부 옮기기 or 상대가 꽉찰때까지 옮기기
while queue:
    temp = queue.popleft()
    buckets= temp[:3]
    for node in range(3):
        for i in dir[node]:
            if buckets[i] + buckets[node] > mat[i]:     #이동시킬 곳의 물의 위치가 꽉차는 case
                temp_bucket = deepcopy(buckets)
                temp_bucket[node] -= mat[i] - temp_bucket[i]
                temp_bucket[i] = mat[i]
                if temp_bucket not in result:
                    queue.append(temp_bucket)
                    result.append(temp_bucket)
            else:
                temp_bucket = deepcopy(buckets)
                temp_bucket[i] += temp_bucket[node]
                temp_bucket[node] = 0
                if temp_bucket not in result:
                    queue.append(temp_bucket)
                    result.append(temp_bucket)

result.sort(key = lambda x: x[2])
result.sort(key = lambda x:x[0])

answer = []
for i in result:
    if i[0]==0:
        answer.append(i[2])
    else:
        break
print(" ".join(map(str, answer)))