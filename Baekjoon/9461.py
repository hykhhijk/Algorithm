import sys

n = int(input())
triangles = [0 for _ in range(100)]
triangles[0]=1
triangles[1]=1
triangles[2]=1

def side_triangle(x):
    if x < 2:
        return triangles[x]
    else:
        if triangles[x]==0:
            triangles[x] = side_triangle(x-2) + side_triangle(x-3)
        return triangles[x]

for _ in range(n):
    num = int(sys.stdin.readline().strip())-1
    result = side_triangle(num)
    print(result)