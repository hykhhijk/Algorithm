n,k = map(int, input().split())

count = 0
while(True):
    if(n == 1):
        break
    elif(n%k ==0):
        n = n/k
        count = count + 1
    else:
        n = n-1
        count = count + 1

print(count)
    

