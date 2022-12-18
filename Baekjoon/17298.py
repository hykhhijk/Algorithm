n = int(input())

num_list = list(map(int, input().split()))
stack = []
result_list=[]

while num_list:
    num = num_list.pop()
    while stack:
        if num >= stack[-1]:
            stack.pop()
        else:
            result_list.append(stack[-1])
            stack.append(num)
            break
    else:
        result_list.append(-1)
        stack.append(num)
result_list.reverse()
print(" ".join(map(str, (result_list))))