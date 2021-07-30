import time
p = input()

start = time.time()
col, row =p[0] ,int(p[1])
col = int(ord(col) - ord('a') + 1)
count = 0
r_temp, c_temp = 0, 0
step = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

#for step in steps이후 step[0], step[1]형식으로 돌리기 가능
for i in range(len(step)):
    r_temp = row + step[i][1]
    c_temp = col + step[i][0]
    if(r_temp < 1 or  r_temp > 8 or c_temp < 1 or c_temp > 8):
        continue
    count += 1

print(count)
print(start - time.time())