N,M,K = map(int,input("Input N,M,K").split())       #python에서 여러 값을 공백에 따라 split()으로 분리
                                                    #map(func, ~)형태로 함수를 적용시켜 map형 저장가능

result=0
temp=list(map(int,input("Input N,M,K").split()))


max_num = max(temp)
temp.remove(max_num)        #remove()는 가장 앞의 max_num값만 제거하므로 중복된 값이 있어도 동작

for j in range(M):
  result += max_num

for k in range(int(M/K)):
  result -= (max_num - max(temp))

print(result)