import sys
from itertools import combinations

while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if num_list[0] ==0:
        break
    del num_list[0]
    num_list.sort()
    combi = combinations(num_list, 6)
    for i in combi:
        for j in i:
            print(j, end=" ")
        print()
    print()