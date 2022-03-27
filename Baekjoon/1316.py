n = int(input())

result = n
sentence = []
for i in range(n):
    temp = input()
    sentence.append(temp)

for i in range(n):
    temp = sentence[i]
    word_list=[]
    for j in range(len(temp)):
        if temp[j] not in word_list:
            word_list.append(temp[j])
        elif temp[j-1] != temp[j]:
            result -= 1
            break


print(result)