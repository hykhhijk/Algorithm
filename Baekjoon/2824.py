import math

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

num1=1
num2=1

for i in n_list:
    num1 *= i
for i in m_list:
    num2 *= i

result = math.gcd(num1, num2)
result = str(result)
if len(result) > 9:
    print(result[-9:])
else:
    print(result)