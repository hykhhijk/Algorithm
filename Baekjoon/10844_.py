n = int(input())
dp_list = [[0]*10 for _ in range(n)]
dp_list[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


###########################################################

# 중요한 점은 점화식 생성이 앞자리 부분이 아니라 뒷자리 부분부터 chk해야 생성이 가능하다는 점이다.

##########################################################


for i in range(1, n):
    for j in range(10):
        if j==0:
            dp_list[i][j] = dp_list[i-1][1]
        elif j==9:
            dp_list[i][j] = dp_list[i-1][8]
        else:
            dp_list[i][j] = dp_list[i-1][j-1] + dp_list[i-1][j+1]


print(sum(dp_list[n-1])%10**9)
            
