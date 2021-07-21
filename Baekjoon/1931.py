n = int(input())

time=[]
result = 0
index = 0
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort()
print(time)
for j in range(n):
    min = 10000000000000
    for i in range(index, n-1, 1):
        if(min > time[i][1]):
            min= time[i][1]
            index=i
            result += 1
        
print(result)