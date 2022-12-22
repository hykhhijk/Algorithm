import sys 
n = int(input())
step_list = [0 for _ in range(301)]
for i in range(n):
    step_list[i] = int(sys.stdin.readline().strip())
dp_list = []
dp_list.append(step_list[0])
dp_list.append(step_list[1] + step_list[0])
dp_list.append(max((step_list[0] + step_list[2]), (step_list[1] + step_list[2])))

for i in range(3, n):
    dp_list.append(max((dp_list[i-2] + step_list[i]), (dp_list[i-3] + step_list[i-1] + step_list[i])))
print(dp_list[n-1])