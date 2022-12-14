import collections
import sys

n = int(input())
for _ in range(n):
    N, M = map(int, sys.stdin.readline().split())
    document_list = list(map(int, sys.stdin.readline().split()))
    document_queue = collections.deque(document_list)
    document_list.sort()
    check_list = [False]*N
    check_list[M] = True
    check_queue = collections.deque(check_list)
    count=0

    while True:
        if document_list[-1]!=document_queue[0]:
            document_queue.append(document_queue.popleft())
            check_queue.append(check_queue.popleft())
        elif document_list[-1]==document_queue[0] and check_queue[0]==False:
            document_list.pop()
            document_queue.popleft()
            check_queue.popleft()
            count+=1
        elif document_list[-1]==document_queue[0] and check_queue[0]==True:
            print(count+1)
            break