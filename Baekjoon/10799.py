input_list = input()

result=0
sticks=0
stack=[]
for i in input_list:
    if i == "(":
        stack.append(i)
        sticks += 1
    elif i == ")":
        index = stack.pop()
        if index == "(":
            result += (sticks-1)
            sticks-=1
        else:
            # result += (sticks)
            result += 1
            sticks -= 1
        stack.append(i)
    # print(sticks, result, i)
# print(result)
# print(sticks)
print(result)