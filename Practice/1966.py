import sys
import copy
from collections import deque

t = int(input())
for _ in range(t):
    answer=0
    n, m = map(int, sys.stdin.readline().split())
    nums = deque(map(int, sys.stdin.readline().split()))
    target = nums[m]
    nums[m]=0
    temp = copy.deepcopy(list(nums))
    temp.sort(reverse=True)
    temp = deque(temp)
    while True:
        tempnum = temp.popleft()
        if target < tempnum:
            while True:
                if nums[0]!=tempnum:
                    nums.append(nums.popleft())
                else:
                    nums.popleft()
                    answer+=1
                    break
        else:
            for i in nums:
                if i==target:
                    answer+=1
                elif i==0:
                    answer+=1
                    break

            print(answer)
            break