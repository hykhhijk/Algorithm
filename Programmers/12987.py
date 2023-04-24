import collections


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = collections.deque(A)
    B = collections.deque(B)
    length = len(A)    
    for i in range(length):
        index=0
        for j in range(len(B)):
            if A[i] < B[j]:
                answer+=1
                index+=1
                break
            else:
                index+=1
        if index==0:
            break
        for _ in range(index):
            B.popleft()
    
    
    
    
    
    return answer