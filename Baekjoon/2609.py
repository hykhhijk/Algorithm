n, m = map(int, input().split())

def divmax(num1, num2):
    remain=1
    while num2!=0:
        num1, num2= num2,num1%num2 
    return num1

def mulmin(num1, num2, divmax):
    mulmin = num1 * num2 / divmax
    return int(mulmin)

divmax = divmax(n, m)
mulmin = mulmin(n, m, divmax)

print(divmax)
print(mulmin)