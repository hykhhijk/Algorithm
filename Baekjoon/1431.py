import sys

n = int(input())

serial_list=[]
sum_list = [0 for _ in range(n)]
for k in range(n):
    serial_list.append(sys.stdin.readline().strip())
    for i in range(len(serial_list[-1])):
        if serial_list[-1][i].isnumeric():
            sum_list[k] += int(serial_list[-1][i])

serial_list.sort(key = lambda x:len(x))
serial_list.sort(key = lambda x:sum_list[x])
