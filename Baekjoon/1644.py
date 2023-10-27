n = int(input())

mat = [False for _ in range(4000001)]
primes = []
answer = 0
for i in range(2, int(4000000**0.5)+1):
    if mat[i]==False:
        temp=2
        while i * temp < 4000000:
            mat[i*temp] = True
            temp+=1
for i in range(2, len(mat)):
    if mat[i]==False:
        primes.append(i)

start = 0
end = 0
interval = 0
if n < 2:
    pass
else:
    while primes[start] <= n+1 and end < len(primes):
        if interval < n:
            interval += primes[end]
            end += 1
        else:
            if interval ==n:
                answer+=1
            interval -= primes[start]
            start += 1
print(answer)