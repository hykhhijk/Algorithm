import sys

n = int(input())

<<<<<<< HEAD
serial_list=[]
sum_list = [0 for _ in range(n)]
for k in range(n):
    serial_list.append(sys.stdin.readline().strip())
    for i in range(len(serial_list[-1])):
        if serial_list[-1][i].isnumeric():
            sum_list[k] += int(serial_list[-1][i])

serial_list.sort(key = lambda x:len(x))
serial_list.sort(key = lambda x:sum_list[x])
=======
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
>>>>>>> 9151601f68bcafa60e01cf3bd0a11b6cf5e7e6d0
