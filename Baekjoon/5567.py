import collections
import sys

n = int(input())
m = int(input())
results = [0 for _ in range(n+1)]
results[1]=1
friends=[[]for _ in range(n+1)]
for _ in range(m):
    friend_temp = list(map(int, sys.stdin.readline().split()))
    friends[friend_temp[0]].append(friend_temp[1])
    friends[friend_temp[1]].append(friend_temp[0])
for i in range(len(friends)):
    friends[i] = list(set(friends[i]))
# print(friends)
q = collections.deque([[1, 1]])
while q:
    index = q.popleft()
    for i in friends[index[0]]:
        if results[i]==0:
            results[i] = index[1]+1
            q.append([i, results[i]])
result=0
for i in results:
    if 2<=i<=3:
        result+=1
print(result)


# for i in range(len(results)):
#     if 2<=results[i] <=3:
#         result+=1
# print(result)
