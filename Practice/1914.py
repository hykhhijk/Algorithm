n = int(input())

bars=[]
bars.append([])
bars.append([5,4,3,2,1])
bars.append([])
bars.append([])


loc = set([1,2,3])
def hanoi(start, target, num):
    if num==1:
        print(start, target)
        return
    else:
        move = loc - set([start, target])
        move = list(move)[0]
        hanoi(start, move, num-1)
        print(start,target)
        hanoi(move,target, num-1)

        


print(2**n-1)
if n <= 20:
    hanoi(1, 3, n)