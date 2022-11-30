import itertools

n = int(input())
num_list = [i for i in range(1, n+1)]

com = list(itertools.permutations(num_list, n))
for i in com:
    for j in i:
        print(j, end=" ")
    print()