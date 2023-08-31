from itertools import permutations

def func(mat):
    result = [abs(mat[i]-mat[i+1]) for i in range(len(mat)-1)]
    return sum(result)


n = int(input())
nums = list(map(int, input().split()))

result=0
perm = permutations(nums, len(nums))
for i in perm:
    temp = func(i)
    if temp > result:
        result = temp


print(result)