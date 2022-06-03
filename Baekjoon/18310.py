n = int(input())

house_list = list(map(int, input().split()))
house_list.sort()


if n==1:
    print(house_list[0])
elif n%2==0:
    print(house_list[len(house_list)//2-1])
else:
    print(house_list[len(house_list)//2])