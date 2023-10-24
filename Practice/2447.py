n = int(input())


def func(n,line):
    if n!=3:
        n= n//3
        func(n, line)
        func(n, line)
        func(n, line)
        func(n, n + line)
        for i in range(n):
            mat[n+line+i].append(" "*n)
        func(n, n + line)
        func(n, 2*n + line)
        func(n, 2*n + line)
        func(n, 2*n + line)


    else:
        mat[line].append("***")
        mat[line+1].append("* *")
        mat[line+2].append("***")




mat = [[] for _ in range(n+1)]
func(n, 1)

for m in mat[1:]:
    print("".join(m))