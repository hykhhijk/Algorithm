wood_list = list(map(int, input().split()))

if wood_list == [1,2,3,4,5]:
    print("1 2 3 4 5")
else:
    while True:
        for i in range(4):
            if wood_list[i] > wood_list[i+1]:
                wood_list[i], wood_list[i+1] = wood_list[i+1], wood_list[i]
                print(" ".join(map(str, wood_list)))
        if wood_list == [1,2,3,4,5]:
            break