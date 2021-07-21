row, col = map(int, input().split())

num = []
for i in range(row):
    num.append(list((map(int, input().split()))))


#2차원list에 map()함수 적용 불가능?
#1row씩 받아와서 반복 돌리는게 최선
for i in range(row):
    result = max(map(min, num))

print(result)