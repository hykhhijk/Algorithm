from collections import defaultdict

nums = defaultdict(int)

a, p = map(int, input().split())
now = str(a)
while True:
    # a = str(a)
    temp=0
    for s in now:
        temp+=int(s)**p
    temp = str(temp)
    if nums[now]!=0:
        break
    nums[now] = temp
    now = temp

result=0
for i in nums.keys():
    if i==now:
        break
    result+=1

print(result)