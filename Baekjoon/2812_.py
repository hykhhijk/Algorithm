n, k = map(int, input().split())

num_list=list(input())

result_list=[]      #지워야할 원소들의 수

for i  in range(n):
    while result_list:
        if k==0:
            break
        elif result_list[-1] < int(num_list[i]):
            result_list.pop()
            k-=1
        else:
            break
    result_list.append(int(num_list[i]))
print("".join(list(map(str, result_list)))) 