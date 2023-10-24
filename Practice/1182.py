from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(1,n+1):
    temp = combinations(nums, i)
    temp = map(sum, temp)
    for j in temp:
        if j == s:
            answer+=1

print(answer)