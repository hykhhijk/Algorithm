n = int(input())

stars = [" "*(n-i-1) + "*"*(i+1) for i in range(n)]

for i in range(len(stars)-2, -1, -1):
    stars.append(stars[i])

for i in range(len(stars)):
    print(stars[i])