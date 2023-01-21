n = int(input())
nums = list(map(int, input().split()))
max_len = len(str(max(nums)))
fill_zero = {}
for i in range(len(nums)):
    fill_zero[nums[i]] = int(str(nums[i]).ljust(max_len, "0"))
nums.sort()
nums.sort(key = lambda x:fill_zero[x], reverse=True)
if sum(nums)==0:
    print(0)
else:
    print("".join(map(str,nums)))