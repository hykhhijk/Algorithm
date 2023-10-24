n = int(input())

for _ in range(n):
    pars = list(input())
    temp=0
    for p in pars:
        if p=="(":
            temp+=1
        elif p==")":
            temp-=1
            if temp < 0:
                temp=1
                break
    if temp != 0:
        print("NO")
    else:
        print("YES")