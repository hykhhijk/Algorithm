n = int(input())
m = int(input())
command = list(map(int, input().split()))
frames = {}
for i in range(len(command)):
    if command[i] not in frames:
        if len(frames)==n:
            temp = 1001
            index = 0
            for k, v in frames.items():
                if v < temp:
                    temp = v
                    index = k
            del frames[index]
        frames[command[i]]=1
    else:
        frames[command[i]]+=1
    
result = []
for i in frames.keys():
    result.append(i)
result.sort()
print(" ".join(map(str, result)))