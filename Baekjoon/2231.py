#list(map(int, str(i))) -> 문자열을 자릿수 별로 순환 
#ex) "123" -> 1,2,3으로 나눌 수 있음
#여기선 sum(map(int, str(str_i)))를 이용하면 각 자릿 수 합을 구할 수 있음

n = input()

sum=0
for i in range(int(n)+1):
    sum=i
    str_i = str(i)
    for j in range(len(str_i)):
        sum += int(str_i[j])
    if(sum == int(n)):
        break
if(i < int(n)):
    print(i)
else:
    print(0)

