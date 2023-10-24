import math
from itertools import combinations

t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))

maxval = max(nums)
mat = [False for i in range(maxval+1)]
primes=[]

for i in range(2, int(math.sqrt(maxval)+1)):
    if mat[i]==False:
        temp=2
        while i*temp < maxval:
            mat[i*temp]=True
            temp+=1

# for p in range(2, len(mat)):
  # if mat[p]==False:
        # primes.append(p)

for n in nums:
    temp=0
    for i in range(2, n//2+1):
        if mat[i]==False and mat[n-i]==False:
            temp+=1
    print(temp)




# for i in nums:
    # print(mat[i])