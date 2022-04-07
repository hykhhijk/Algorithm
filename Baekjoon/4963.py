import sys
sys.setrecursionlimit(10000)

# answer=[]
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    mat=[]
    for _ in range(h):
        mat.append(list((map(int, input().split()))))

    count = 0
    def bfs(x, y):
        if x < 0 or x > h-1 or y < 0 or y > w-1:
            return False
        elif mat[x][y]==1:
            mat[x][y]=0
            bfs(x+1, y-1)
            bfs(x+1, y)
            bfs(x+1, y+1)
            bfs(x, y+1)
            bfs(x, y-1)
            bfs(x-1, y+1)
            bfs(x-1, y)
            bfs(x-1, y-1)
            return True 
        elif mat[x][y]==0:
            return False
        return False




    for i in range(h):
        for j in range(w):
            if mat[i][j]==1:
                count += bfs(i, j)
    print(count)
