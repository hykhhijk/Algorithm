import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    result=0
    expr = sys.stdin.readline().strip()
    for i in expr:
        if i=="(":
            result+=1
        elif i==")":
            result-=1
            if result <0:
                print("NO")
                break
    if result==0:
        print("YES")
    elif result>0:
        print("NO")