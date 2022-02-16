n = input()

index = len(n)/2

count_1=0
count_2=0
for i in range(int(index)):
    count_1 += int(n[i])
    count_2 += int(n[-i-1])


if count_1 == count_2:
    print("LUCKY")
else:
    print("READY")