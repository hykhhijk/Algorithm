import collections

n, k = map(int, input().split())
temp_list = [str(i) for i in range(1, n+1)]
queue = collections.deque(temp_list)
result=[]

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end="")
print(", ".join(result), end="")
print(">")    