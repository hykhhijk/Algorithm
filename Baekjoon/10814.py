import sys

n = int(input())

c_dict=[]
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    c_dict.append((age, name))

c_dict.sort(key = lambda x: (x[0]))

for i in c_dict:
    print(i[0], i[1])