n = int(input())

time=[]
result = 0
index = 0
j=0
for i in range(n):
    time_temp = []
    start, end = map(int, input().split())
    time.append([start,end])

#파이썬 2차원리스트 리스트 내부 원소 값 정렬예시
#예에서 두번째 원소를 정렬하였는데 이 전에 미리 sort()를 함으로써 두번째 원소 값이 같을 시 첫번째 원소를 기준으로 정렬하였음
time.sort()
time = sorted(time, key=lambda x:x[1])

for i in range(len(time)):
    if(index <= time[i][0]):
        index = time[i][1]
        result += 1

print(result)

