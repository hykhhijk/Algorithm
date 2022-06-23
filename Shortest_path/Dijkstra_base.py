import sys

input = sys.stdin.readline
INF = int(1e9)      #보통 C/C++ 사용자 고려를 위하여 1억 이하로 제한됨

n,m = map(int, input().split())
start = int(input())    #시작노드 입력
graph = [[] for _ in range(n+1)]        #각 노드에 대한 연결 리스트 생성

visited = [False] * (n+1)               #방문 체크를 위한 리스트
distance = [INF] * (n+1)                #거리 저장을 위한 리스트

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))             #a노드에서 b노드로 가는 거리가 c이다

#방문하지 않은 노드를 위한 탐색
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]       #시작 노드에서 한번에 갈 수 있는 모든 노드에 대한 거리 초기화

    for _ in range(n-1):            
        now = get_smallest_node()   #방문한 노드 중 가작 가까운 노드부터 하나씩 꺼낸다
        visited[now] = True         #방문 표시해서 get_smallest_node가 두번 적용되지 않게함
        
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:   #현재까지 최소거리 distance보다 cost가 작다면 값을 update
                distance[j[0]] = cost

dijkstra(start)