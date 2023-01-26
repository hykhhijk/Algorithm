import sys

n = int(input())
car_in = []
car_out = []
for _ in range(n):
    car_in.append(sys.stdin.readline().rstrip())
for _ in range(n):
    car_out.append(sys.stdin.readline().rstrip())

result = 0
index = 0
for i in range(len(car_out)):
    if car_in[index] == car_out[i]:
        index +=1
        continue
    else:
        car_in.remove(car_out[i])
        result+=1

print(result)
