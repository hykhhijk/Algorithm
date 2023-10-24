n = int(input())
nums = list(map(int, input().split()))

sortnums = sorted(list(set(nums)))

dicts = {}
for i in range(len(sortnums)):
    dicts[sortnums[i]] = i

for n in nums:
    print(dicts[n], end=" ")