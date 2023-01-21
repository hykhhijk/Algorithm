n =input()
n = list(map(int, n))
check = 0
check0 = False
for i in n:
    check += i
    if i==0:
        check0=True
if check0==True and check%3==0:
    n.sort(reverse=True)
    print("".join(map(str, n)))
else:
    print(-1)