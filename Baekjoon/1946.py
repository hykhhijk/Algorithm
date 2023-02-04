import sys

t = int(input())

for _ in range(t):
    n = int(input())
    mat = []    
    for _ in range(n):
        mat.append(list(map(int, sys.stdin.readline().split())))
    result_left = []
    # result_right = []
    mat_left = sorted(mat)    
    # mat_right = sorted(mat,key = lambda x:x[1])
    result_left.append(mat_left[0])
    # result_right.append(mat_right[0])
    for i in range(1, len(mat)):
        if mat_left[i][1] < result_left[-1][1]:
            result_left.append(mat_left[i])
        # if mat_right[i][0] < result_right[-1][0]:
            # result_right.append(mat_right[i])
    print(len(result_left))
