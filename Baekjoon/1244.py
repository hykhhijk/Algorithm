import sys

n = int(input())
switch_list = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    sex, switch = map(int, sys.stdin.readline().split()) 
    if sex==1:
        temp = switch
        while switch <= n:
            switch_list[switch-1] -=1
            switch_list[switch-1] = abs(switch_list[switch-1])
            switch += temp
    else:
        index = 1
        switch_list[switch-1] -=1
        switch_list[switch-1] = abs(switch_list[switch-1])
        while True:
            left, right = switch-index, switch +index
            if left < 1 or right > n:
                break
            elif switch_list[left-1]==switch_list[right-1]:
                switch_list[left-1] -=1
                switch_list[left-1] = abs(switch_list[left-1])
                switch_list[right-1] = switch_list[left-1]
                index += 1
            else:
                break
        
result = []
for i in range(len(switch_list)):
    result.append(str(switch_list[i]))
    if len(result)>19:
        print(" ".join(result))
        result = []
print(" ".join(result))
