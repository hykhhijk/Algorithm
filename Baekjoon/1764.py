import sys

n, m = map(int, input().split())

name_dict={}
result=[]

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    name_dict[name] = 0

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name in name_dict:
        result.append(name)

result.sort()
print(len(result))
for i in result:
    print(i)