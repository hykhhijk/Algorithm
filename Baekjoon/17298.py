n = int(input())

num_list = list(map(int, input().split()))
# num_list = num_list.reverse()
num_list.reverse()
big_list=[]
result_list=[]
for i in num_list:
    while big_list:
        if big_list[-1] <= i:
            big_list.pop()
        else:
            result_list.append(big_list[-1])
            break
    
    if len(big_list)==0:
        result_list.append(-1)
    big_list.append(i)

result_list.reverse()
print(" ".join(map(str, result_list)))