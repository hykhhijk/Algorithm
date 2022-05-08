import sys


n = int(input())
# for _ in range(n):
num_list =map(int, sys.stdin.readline().split())
num_list.sort() 
m = int(input())
# for _ in range(m):
chk_list = map(int, sys.stdin.readline().split())
result_list=[]

for i in chk_list:
    start=0
    end=len(num_list)-1
    while True:
        mid = (start+end)//2
        # print(start, mid, end)

        if start > end:
            sys.stdout.write("0"+"\n")
            break
        elif num_list[mid]==i:
            sys.stdout.write("1"+"\n")
            break
        elif i < num_list[mid]:
            end = mid-1
        else:
            start = mid+1

# print(result)
# for i in range(len(chk_list)):
#     if chk_list[i] in result_list:
#         sys.stdout.write("1"+"\n")
#     else:
#         sys.stdout.write("0"+"\n")