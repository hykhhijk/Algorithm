n = int(input())


tower_list = list(map(int, input().split()))

result_list=[]
tower_left_list=[]


for i in range(n):
    # index, tower = i, tower_list[i]
    if len(tower_left_list) != 0:
        while tower_left_list:
############################################################
        #기존은 tower_left_list[::-1]방식으로 순회했지만 이는 pop()연산을 반영하지 못하므로
        #순회시간을 단축시키지 못한다는점에 주의할 것
############################################################

            if tower_list[i] < tower_left_list[-1][0]:
                result_list.append(tower_left_list[-1][1])
                break
            elif tower_list[i] > tower_left_list[-1][0]:
                tower_left_list.pop()
        # tower_left_list.append([tower, index])

    if len(tower_left_list) == 0:
        result_list.append(0)
    # print(tower_left_list)
    tower_left_list.append([tower_list[i], i+1])

# print(result_list)
# print(tower_left_list)
# print(" ".join(result_list))
print(" ".join(map(str, result_list)))
