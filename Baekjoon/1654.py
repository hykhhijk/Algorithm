import sys

n, m = map(int, sys.stdin.readline().split())


tree_list=[]
for i in range(n):
    tree_list.append(int(sys.stdin.readline().rstrip()))


start=1
result=0
end=max(tree_list)
while True:
    mid = (start+end)//2
    count=0
    for i in range(len(tree_list)):
        count+=tree_list[i]//mid
    
    if count < m:
        end = mid-1
    elif start>mid:
        result = mid
        break
    else:
        start = mid+1

print(result)


    