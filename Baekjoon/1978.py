n = int(input())

num_list = list(map(int, input().split(" ")))


def check(num):
    for i in range(2, num+1):
        if i ==num:
            return 1
        elif num%i == 0:
            return 0
    if num==1:
        return 0


result=0
for i in num_list:
    result += check(i)
print(result)