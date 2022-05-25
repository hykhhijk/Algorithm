temp_list = list(input())

num_list=[]
for i in range(len(temp_list)):
    num_list.append(int(temp_list[i]))
num_list.sort(reverse=True)
for i in num_list:
    print(i, end="")