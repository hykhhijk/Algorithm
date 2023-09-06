import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()
nums = deque(nums)
result = 0

while len(nums) >2:
    if nums[0] <= 0 and nums[1] <= 0:
        left = nums.popleft()
        right = nums.popleft()
        result += left * right
    elif nums[-1] > 0 and nums[-2] > 0:
        right = nums.pop()
        left = nums.pop()
        if left==1 or right==1:
            result += (left + right)
        else:
            result += left * right

if len(nums) <= 1:
    result += sum(nums)
else:
    if sum(nums) > nums[0] * nums[1]:
        result += sum(nums)
    else:
        result += nums[0] * nums[1]

print(result)

