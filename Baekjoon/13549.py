import heapq

n, m = map(int, input().split())
graph = [0 for _ in range(m+1)]
distance = [10**10 for _ in range(200001)]


def dijkstra(start):
    q = []
    if start==0:
        heapq.heappush(q, [1, 1])
        distance[1]=1
    else:
        heapq.heappush(q, [0, start])
        distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if now==m:
            return dist
        if distance[now] < dist:
            continue
        for i in [now+1, now-1, now*2]:
            if 0 <= i <= 200000 and distance[i]==10**10:
                if i==now*2:
                    distance[i] = distance[now]
                    heapq.heappush(q, [distance[i], i])
                elif distance[now]+1 < distance[i]:
                    distance[i] = distance[now]+1
                    heapq.heappush(q, [distance[i], i])
result = dijkstra(n)
print(result)