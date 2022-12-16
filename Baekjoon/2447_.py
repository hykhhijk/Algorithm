n = int(input())


def star(n):
    if n==0:
        print("*", end="")
        return

    star(n-1)
    star(n-1)
    star(n-1)
    print()
    star(n-1)
    if n==1:
        print(" ", end="")
    else:
        for i in range(n*3):
            for j in range(n*3):
                print(" ", end="")
            print()
    star(n-1)
    print()
    star(n-1)
    star(n-1)
    star(n-1)

star(n)