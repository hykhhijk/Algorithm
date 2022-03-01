n = int(input())


result = [0]*n
for i in range(n):
    mat = input()
    for j in range(len(mat)):
        if mat[j] == "(":
            result[i] += 1
        elif mat[j] == ")" :
            if result[i] <= 0:
                result[i] -= 1
                break
            else:
                result[i] -= 1

for i in range(n):
    if result[i] == 0:
        print("YES")
    else:
        print("NO")
            
