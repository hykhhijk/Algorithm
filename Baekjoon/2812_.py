n, k = map(int, input().split())
K=k
num_list=list(input())

result_list=[]      #지워야할 원소들의 수
small_list=[]

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
if len(result_list) >= n-K:
    print("".join(list(map(str, result_list[:n-K])))) 
else:
    print("".join(list(map(str, result_list)))) 