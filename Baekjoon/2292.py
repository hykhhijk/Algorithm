import sys
num = int(sys.stdin.readline().rstrip())
result=1
if num==1:
    print(1)
else:
    num-=1
    index = 6
    while True:
        num -= index
        result+=1
        index+=6
        if num <= 0:
            print(result)
            break
