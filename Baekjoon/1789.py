n = int(input())
result = 0
index=  1
while True:
    result += index
    if result > n:
        break
    index+=1
print(index-1)