import sys

n = int(input())

prices = list(map(int, sys.stdin.readline().split()))
budget = int(input())

def check(mid):
    temp = 0
    for i in range(len(prices)):
        if prices[i] <= mid:
            temp+= prices[i]
        else:
            temp += mid
    return temp


if sum(prices) <= budget:
    print(max(prices))
else:
    start, end = 0, 100000
    while start <= end:
    # while start != end:
        mid = (start + end)//2
        price = check(mid)
        if price > budget:
            end = mid-1
        else:
            start = mid+1

    mid = (start + end)//2
    if check(mid) > budget:
        print(mid-1)
    else:
        print(mid)