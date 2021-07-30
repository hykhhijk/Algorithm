import time


n = int(input())

row = 1
col = 1



direction = list(map(str, input().split()))

start = time.time()
for i in range(len(direction)):
    if(direction[i] == "R"):
        col += 1
        if(col == n + 1):
            col -= 1
    elif(direction[i] == "L"):
        col -= 1
        if(col == 0):
            col += 1
    elif(direction[i] == "U"):
        row -= 1
        if(row == 0):
            row += 1
    elif(direction[i] == "D"):
        row += 1
        if(row == n + 1):
            row -= 1






print(row, col)

print("Time: ", time.time() - start)