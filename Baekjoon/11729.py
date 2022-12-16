n = int(input())
location=set([1,2,3])

def hanoi(n, start, end):
    if n==1:
        print(start, end)
        return
    else:
        move = location - set([start, end]) 
        move = list(move)[0]          
        hanoi(n-1, start, move)
        print(start, end)
        hanoi(n-1, move, end)

print(2**n-1)
hanoi(n, 1, 3)
