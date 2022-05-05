n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split(" "))
    room = (n//h)+1
    if n%h==0:
        room-=1
    floor = n%h
    if floor==0:
        floor = h
    print(str(floor), end="")
    print(str(room).rjust(2, "0"))