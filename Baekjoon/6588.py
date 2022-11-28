import sys

prime_mat = [False, False] + [True for _ in range(1000000)]

for i in range(2, int(1000000**0.5+1)):
    if prime_mat[i] == True:
        temp = 2
        while i*temp < 1000001:
            prime_mat[i*temp] = False
            temp += 1
while True:
    n = int(sys.stdin.readline().strip())
    if n==0:
        break
    min_n = 3
    max_n = n-3
    while True:
        if prime_mat[min_n]==True and prime_mat[max_n]==True:
            print(n, "=", min_n,"+",max_n)    
            break
        elif min_n > int(n/2)+1:
            print("Goldbach's conjecture is wrong.")
        else:
            min_n+=2
            max_n-=2
