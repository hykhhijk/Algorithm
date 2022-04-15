n = int(input())

stair=[0]
for i in range(n):
    stair.append(int(input()))
visit = stair.copy()

print(stair)
count = 0
for i in range(2, len(stair)):
    temp = stair[i]
    if count >= 1 or i+1 >= len(stair) or visit[i-1] < visit[i-2]:
        stair[i] = stair[i] + stair[i-2]
        count = 0
        
    elif visit[i-1] >= visit[i-2]:     
        stair[i] = stair[i] + stair[i-1]
    if stair[i] == temp + stair[i-1]:
        count += 1
    elif stair[i] == temp + stair[i-2]:
        count=0
print(stair)
print(stair[-1])    