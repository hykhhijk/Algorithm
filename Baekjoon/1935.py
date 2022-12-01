n = int(input())

expr_temp = input()

num_list=[]
str_num_dict={}
for i in range(n):
    num = input()
    str_num_dict[chr(65+i)] = num
    # expr = expr.replace(chr(65+i), num)

expr=[]
for i in expr_temp:
    if i in ["+", "-", "*", "/"]:
        expr.append(i)
    else:
        expr.append(str_num_dict[i])

for i in range(len(expr)):
    if expr[i] in ["+", "-", "*", "/"]:
        num2 = float(num_list.pop())
        num = float(num_list.pop())
        operate = expr[i]
        if operate=="+":
            result = num+num2
        elif operate=="-":
            result = num-num2
        elif operate=="*":
            result = num*num2
        elif operate=="/":
            result = num/num2
        # print(operate)
        # print(num, num2)
        num_list.append(result)

    else:
        num_list.append(expr[i])

print(f"{round(num_list[0], 3):.2f}")