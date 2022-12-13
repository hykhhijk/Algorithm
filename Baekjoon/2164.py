import collections

num = int(input())
card_list = [i+1 for i in range(num)]
queue = collections.deque(card_list)

while True:
    if len(queue)==1:
        break
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])