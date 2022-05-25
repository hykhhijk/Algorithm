import sys

n = int(input())

str_list=[]
len_list=[]
for _ in range(n):
    temp_str = sys.stdin.readline().rstrip()
    str_list.append(temp_str)
    len_list.append(len(temp_str))

def str_len(array):
    return len(array)

str_list.sort()
str_list = sorted(str_list, key=str_len)

for i in range(len(str_list)):
    if i == len(str_list)-1:
        print(str_list[i])
    elif str_list[i] != str_list[i+1]:
        print(str_list[i] )