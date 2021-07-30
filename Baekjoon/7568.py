n = int(input())
p=[]
for _ in range(n):
    p.append(list(map(int, input().split())))

for i in range(n):
    max=0
    for j in range(n):
       if(max <= p[j][1]):
           max=p[j][1]