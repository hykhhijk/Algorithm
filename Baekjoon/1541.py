n = input()
nums = []
index = 0
for i in range(len(n)):
    if n[i]=="+"or n[i]=="-":
        nums.append(int(n[index:i]))
        index = i
nums.append(int(n[index:]))

result = 0
temp = 0
minus=False
for i in range(len(nums)):
    if nums[i] > 0:
        if minus==False:
            result += nums[i]
        else:
            result -= nums[i]
    else:
        result += nums[i]
        minus=True
print(result)