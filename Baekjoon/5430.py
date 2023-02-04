import sys
import collections

t = int(input())

for _ in range(t):
    command = list(sys.stdin.readline().strip())
    trash = sys.stdin.readline()
    num_list = sys.stdin.readline().strip()
    if len(num_list)==2:
        num_list = collections.deque([])
    else:
        num_list = num_list[1:-1].split(",")
        num_list = collections.deque(num_list)
    result_list = []
    reverse=False
    error=False

    for i in command:

        if i == "R":
            if reverse == False:
                reverse=True
            else:
                reverse = False
        if i == "D":
            if len(num_list)!=0:
                if reverse == False:
                    result_list.append(num_list.popleft())
                else:
                    result_list.append(num_list.pop())
            else:
                print("error")
                error = True
                break
    if not error:
        print("[", end="")
        if reverse == True:
            num_list.reverse()
        else:
            pass
        print(",".join(num_list), end="")
        print("]")
    else:
        continue
