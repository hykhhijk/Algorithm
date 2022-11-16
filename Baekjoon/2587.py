num_list=[]
for i in range(5):
    num_list.append(int(input()))

num_list.sort()
sum = num_list[0] + num_list[1] + num_list[2] + num_list[3] + num_list[4] 
sum = sum//5
median = num_list[2]

print(sum)
print(median)