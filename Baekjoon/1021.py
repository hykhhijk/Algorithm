import collections

n, m = map(int, input().split())

target_list = list(map(int, input().split()))
num_list = [i for i in range(1, n+1)]
queue = collections.deque(num_list)
count=0

for i in target_list:
    while True:
        if queue[0]==i:
            queue.popleft()
            break
        elif len(queue) - queue.index(i) > len(queue)//2:
            queue.append(queue.popleft())
            count+=1
        else:
            queue.appendleft(queue.pop())
            count+=1
        # print(queue)
print(count)
