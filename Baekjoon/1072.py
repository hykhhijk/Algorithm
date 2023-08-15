import math

x, y = map(int, input().split())

win_rate = y / x
# win_rate = math.floor(win_rate * 100)
win_rate = (y*100)//(x)
if win_rate >=99:
    print(-1)
else:
    start, end = 0, x
    while start <= end:
        mid = (start + end)//2
        # if math.floor((y + mid) / (x + mid) * 100) > win_rate:
        if ((y + mid) * 100 ) // ((x + mid)) > win_rate:

            end  = mid-1
            result = mid
        else:
            start = mid+1
        # print(math.floor((y + mid) / (x+mid) * 100), mid)
    print(result)
