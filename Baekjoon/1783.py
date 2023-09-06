n, m = map(int, input().split())

row, col = 0, 0
if n > 2 and m > 6:
    row, col = 0, 7
    rightmove = m - col
    # upmove = max(n//2, rightmove)
    print(rightmove+5)
else:
    if n==1:
        print(1)
    elif n==2:
        print(min((m-col -1)//2 + 1, 4))
    elif n > 2:
        print(min(m, 4))