from cmath import inf
n = int(input())



count_list=[inf]*(n+1)


for i in range(2, n+1):
    if i==2 or i==3:
        count_list[i]=1    
    else:
        if i%6==0:
            count_list[i] = min(count_list[i//3]+1,count_list[i//2]+1, count_list[i-1]+1)
        elif i%3==0:
            count_list[i] = min(count_list[i//3]+1, count_list[i-1]+1)
        elif i%2==0:
            count_list[i] = min(count_list[i//2]+1, count_list[i-1]+1)
        else:
            count_list[i] = count_list[i-1]+1
            
if n==1:
    print(0)
else:
    print(count_list[n])