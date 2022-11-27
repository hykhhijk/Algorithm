import itertools

n,m = map(int, input().split())
perm_list=[i for i in range(1, n+1)]
permutations = itertools.permutations(perm_list, m)
permutations = list(permutations)
for i in permutations:
    for j in i:
        print(j, end=" ")
    print()