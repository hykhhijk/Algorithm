n = input()

result_str = []
result_int = 0
for i in range(len(n)):
####### data.isalpha() or data.isdigit()을 사용하면 노가다 필요없음

    if n[i]=="0" or n[i]=="1" or n[i]=="2" or n[i]=="3" or n[i]=="4" or n[i]=="5" or n[i]=="6" or n[i]=="7" or n[i]=="8" or n[i]=="9":
        result_int += int(n[i])
    else:
        result_str.append(n[i])
result_str.sort()
for i in range(len(result_str)):
    print(result_str[i], end="")
print(result_int)