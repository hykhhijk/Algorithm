from collections import deque
from collections import defaultdict
import math

a, b = map(int, input().split())
queue = deque([[a, 1]])
dicts = defaultdict(int)


while queue:
    loc, dist = queue.popleft()
    if dicts[loc]==0:
        dicts[loc] = dist
        if (loc*10) + 1 <= b:
            queue.append([(loc*10) + 1, dist+1])  
        if loc*2 <= b:
            queue.append([loc*2, dist+1])

if dicts[b]==0:
    print(-1)
else:
    print(dicts[b])