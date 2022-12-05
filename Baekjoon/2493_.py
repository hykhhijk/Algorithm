n = int(input())


tower_list = list(map(int, input().split()))

result_list=["0"]
tower_left_list=[]


for index, tower in enumerate(tower_list):
    count=0
    for k, i in enumerate(tower_left_list[::-1]):
        if i[0] > tower:
            result_list.append(str(i[1]+1))
            break

        elif i == tower_left_list[0]:
            result_list.append(str(0))
        elif i[0] < tower:
            # print(tower_left_list)
            # print(k)
            tower_left_list.pop(k-count)
            count+=1
            continue
    # print(tower_left_list)
    tower_left_list.append([tower, index])

# print(tower_left_list)
print(" ".join(result_list))