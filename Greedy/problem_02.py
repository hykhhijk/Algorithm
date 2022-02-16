n = input()

result=0
for i in range(len(n)):
    if result==0 or result==1 or n[i]=="0" or n[i]=="1":
        result += int(n[i])
    else:
        result *= int(n[i])
print(result)

