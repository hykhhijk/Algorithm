n, m = map(int, input().split())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

def cctv1(x, y, space, counter):
    if x < 0 or x >= n or y < 0 or y>=m or mat[x][y]==6:
        return space-1
    if counter==0:
        if mat[i][j]==0:
            dist = cctv1(x+1, y, space+1, 0)
        else:
            dist = cctv1(x+1, y, space, 0)
    elif counter==1:
        dist = cctv1(x-1, y, space+1, 1)
        
    elif counter==2:
        dist = cctv1(x, y+1, space+1, 2)
    elif counter==3:        
        dist = cctv1(x, y-1, space+1, 3)
    return dist





for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]==1:
            for k in range(4):
                temp = cctv1(i, j, 0, k)
                print(temp)
