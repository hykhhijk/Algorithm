import sys


n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline().strip()))
houses.sort()

start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end)//2
    value = houses[0]
    count = 1

    for i in range(len(houses)):
        if houses[i] >= value + mid:
            value = houses[i]
            count+=1

    if count >= c:          #count > c로는 풀리지 않음-> 조건을 만족하면서 최적인 케이스를 찾고 싶은것이기 때문에 간격을 계속 넓혀주는쪽으로 진행하는게 맞다?
        start = mid + 1
    else:
        end = mid -1

if count >= c:
    print(mid)
else:
    print(mid-1)