import heapq


def solution(n, k, enemy):

    removes = []
    max_enemy = 0
    for i in range(len(enemy)):
        if len(removes) < k:
            heapq.heappush(removes, enemy[i])
        elif enemy[i] > removes[0]:
            n -= heapq.heappop(removes)
            heapq.heappush(removes, enemy[i])
        else:
            n -= enemy[i]
        if n < 0:
            i -=1   #n이 0보다 아래이면 i 보다 한인덱스 앞이 최선
            break
            
    answer = i+1    #인덱스 맞추기용
    return answer