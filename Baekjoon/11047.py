n,k = map(int, input().split())

coin=[]
result = 0
for i in range(n):
    coin.append(int(input()))


#range 범위확인[:: -1]형태 가능
#중간에 continue하나 들어가 있는 부분은 무의미한 코드임

for i in  range(n-1, -1, -1):
    if(k == 0):
        break
    elif(k < coin[i]):
        continue
    elif(k >= coin[i]):
        result += int(k/coin[i])
        k %= coin[i]
    


print(result)


