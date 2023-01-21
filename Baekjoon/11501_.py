import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    num_reverse = sorted(nums, reverse=True)
    index=0
    stack = []
    result=0
    for i in range(len(nums)):
        if nums[i]!=num_reverse[index]:
            stack.append(nums[i])
        else:
            index+=1
            while stack:
                temp = stack.pop()
                if temp==num_reverse[index]:
                    index+=1
                result += nums[i]- temp
    print(result)