from collections import  deque
import sys

t = int(input())
for _ in range(t):
    start, end = map(int,sys.stdin.readline().split())
    check = [False] * 10001
    check[int(start)] = True
    queue = deque([[int(start), ""]])
    while queue:
        num, com = queue.popleft()
        if num==end:
            break
        nnum, ncom= num*2%10000, com+"D"
        if check[nnum]==False:
            check[nnum] = True
            queue.append([nnum, ncom])

        nnum, ncom = num-1,com+"S"  
        if nnum < 0: 
            nnum = 9999       
        if check[nnum]==False:
            check[nnum] = True
            queue.append([nnum, ncom])


        nnum, ncom =num//1000 + (num%1000) * 10, com+"L"         
        if check[nnum]==False:
            check[nnum] = True
            queue.append([nnum, ncom])


        nnum, ncom = (num%10)*1000 +num//10 ,com+"R"         
        if check[nnum]==False:
            check[nnum] = True
            queue.append([nnum, ncom])

    print(com)