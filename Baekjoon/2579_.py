import sys 
n = int(input())
step_list = []
index = False

for _ in range(n):
    step_list.append(int(sys.stdin.readline().strip()))
dp_list = step_list.copy()

dp_list = [0 for _ in range(301)]

def step(x, index):
    if x==0:
        return dp_list[0]
    elif x==1:
        if index == False:
            return dp_list[1] + dp_list[0]
        else:
            return dp_list[1]
    if index == True:
        dp_list[x] = step(x-2, False)
    else:
        dp_list[x] = dp_list[x] + max(step(x-2, False), step(x-1, True))
    return dp_list[x]


step(n-1, index)
print(dp_list)