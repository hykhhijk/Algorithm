n = int(input())

mat_list = [[]for _ in range(n)]

def star(x, row):
    if x==3:
        mat_list[row].append("***")
        mat_list[row+1].append("* *")
        mat_list[row+2].append("***")
    else:
        x = x//3
        for _ in range(3):
            star(x, row)    
        star(x, row+x)
        for i in range(x):
            for _ in range(x):
                mat_list[row+i+x].append(" ")
        star(x, row+x)
        for _ in range(3):
            star(x, row + 2*x) 
                


star(n, 0)

for i in mat_list:
    print("".join(i))    