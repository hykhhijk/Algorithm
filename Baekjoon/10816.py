n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
needs = list(map(int, input().split()))

dict = {i:0 for i in set(cards + needs)}
for i in range(len(cards)):
    dict[cards[i]]+=1

result=[]
for i in range(len(needs)):
    result.append(dict[needs[i]])
print(" ".join(map(str, result)))