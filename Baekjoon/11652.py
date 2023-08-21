from collections import defaultdict
import sys

cards = defaultdict(int)


n = int(input())
for _ in range(n):
    index = int(sys.stdin.readline().strip())
    cards[index] += 1

temp = 0
index = sorted(cards.items())
cards = dict(index)

for k, v in cards.items():
    if v > temp:
        temp = v
        result=k

print(result)