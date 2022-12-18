import sys

n = int(input())

serial_list = []
sum_dict = {}
for _ in range(n):
    serial = sys.stdin.readline().strip()
    sum_dict[serial] = 0
    for i in serial:
        if i.isnumeric():
            sum_dict[serial] += int(i)
    serial_list.append(serial)

serial_list.sort()
serial_list.sort(key = lambda x: sum_dict[x])
serial_list.sort(key = lambda x: len(x))

for i in serial_list:
    print(i)