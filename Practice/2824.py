n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

num1 = 1
num2 = 1
for i in ns:
    num1*=i
for j in ms:
    num2*=j

while num2!=0:
    num1, num2 = num2, num1%num2 
if len(str(num1))>9:
    print(str(num1)[-9:])
else:
    print(num1)