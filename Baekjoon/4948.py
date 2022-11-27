prime_list=[True for _ in range(246912*2+1)]
prime_list[0]=False
prime_list[1]=False

for i in range(2, int(246912**0.5+1)):
    temp=2
    while i*temp <= 246912:
        prime_list[i*temp]=False
        temp+=1



while True:
    n = int(input())
    if n==0:break
    else:
        count_list=prime_list[n+1:n*2+1]
        print(count_list.count(True))