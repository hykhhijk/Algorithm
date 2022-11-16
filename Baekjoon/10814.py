import sys

n = int(input())

c_dict=[]
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age.zfill(3)
    c_dict.append(age+name)