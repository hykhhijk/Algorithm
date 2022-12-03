import sys

n = int(input())
num_list = [n-i for i in range(n)]
move_list=[]

target_list=[]
for _ in range(n):
    target_list.append(int(sys.stdin.readline().strip()))

def stack(result):
    for i in target_list:
        while len(num_list)>0 and num_list[-1] <= i:
            move_list.append(num_list.pop())
            result.append("+")
            # print(num_list)
        else:
            while True:
                if len(move_list) == 0:
                    print("NO")
                    return False
                temp = move_list.pop()
                result.append("-")
                if temp==i:
                    break
    return result

result=[]
result = stack(result)
# print(result)
if result != False:
    for i in result:
        print(i)