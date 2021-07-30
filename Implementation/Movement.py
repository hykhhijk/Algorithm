#다시 풀기




n,m = map(int, input().split())
row ,col, dir = map(int, input().split())

land = [[0] * m for _ in range(n)]
print(land)

for i in range(n):
    land[i] = (list(map(int, input().split())))

while(True):
 for i in range(3,0,-1):
     if()
     elif(dir==3):
        if(land[row][col-1]==0):
            land[row][col] = 1
            col -= 1
        else:
            break
     elif(dir==2):
        if(land[row-1][col]==0):
            land[row][col] = 1
            row -= 1
        else:
            break
     elif(dir==1):
        if(land[row][col+1]==0):
            land[row][col] = 1
            col += 1
        else:
            break
     elif(dir==0):
        if(land[row+1][col]==0):
            land[row][col] = 1
            row += 1
        else:
            break
    
