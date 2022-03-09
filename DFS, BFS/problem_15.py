from collections import deque

n, m, k, x = map(int, input().split())
result, count = 0, 0

city_list = [[0] for _ in range(m+1)]
queue = deque()
for i in range(m):
    start, end = map(int, input().split())
    if city_list[start][0] == 0:
        city_list[start][0] = end
    else:
        city_list[start].append(end)


queue.append(x)
while(True):
    next = queue.popleft()
    if city_list[next][0] == 0:
        continue
    else:
        if count == k:
            result = len(city_list[next])
            break
        else:
            for i in range(len(city_list[next])):
                queue.append(city_list[next][i])
                count+=1
print(result)

##### 음... "최단"거리에서 조졌다
##### 거리에 관한걸 n길이의 distance배열에 넣어본다음 풀어보자