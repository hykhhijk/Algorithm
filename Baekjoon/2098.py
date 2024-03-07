import sys

INF = 1e+9
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
    
dp = [[None for _ in range(1<<n)] for _ in range(n)]    #모든 방문 가능 경우의 수
chk = 1

###############################
#9번줄과 25번줄에 None이 아니라 INF를 사용할 시 시간 초과
###############################



def search(node, chk):
    if chk==(1<<n)-1:
        if mat[node][0]!=0:
            return mat[node][0]
        else:
            return INF

    if dp[node][chk]!=None: 
        return dp[node][chk]

    min_value = INF
    for i in range(1, n):
        if (mat[node][i]!= 0) and ((chk & (1<<i))==0):    #연결되어 있으며 방문한적 없을때
            min_value = min(min_value, search(i, chk | (1<<i)) + mat[node][i])
    dp[node][chk] = min_value

    return min_value


answer = search(0,chk)
print(answer)