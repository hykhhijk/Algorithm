import sys

n,m = map(int, sys.stdin.readline().split())

tree_list = list(map(int, sys.stdin.readline().split()))
start=1
end=max(tree_list)
while True:
    count=0
    mid = (start+end)//2

    for i in tree_list:
        if i > mid:
            count+=i-mid

    if count >= m:
        start=mid+1
        if start > end:
            print(end)
            break
    elif count==m:
            print(end)
            break
    else:
        end = mid-1
        if start > end:
            print(end)
            break