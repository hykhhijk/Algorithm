import sys

n,m = map(int, sys.stdin.readline().split())

tree_list = list(map(int, sys.stdin.readline().split()))
print(tree_list)
start=0
end=max(tree_list)
while True:
    count=0
    mid = (start+end)//2
    for i in range(len(tree_list)):
        count+=tree_list[i]-mid
    if count > m:
        start=mid+1
    elif start > mid:
        print(mid)
        break
    else:
        end = mid-1

    