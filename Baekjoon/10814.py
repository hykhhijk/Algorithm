import sys

n = int(input())

c_dict={}
for _ in range(n):
    age, name = sys.stdin.readline().split()
    c_dict[name] = age


print(c_dict.items())
c_dict = sorted(c_dict.items())
print(c_dict)