import itertools

n, m =map(int, input().split())

num_list = [i+1 for i in range(n)]
combination_list = itertools.combinations(num_list, m)

for i in combination_list:
    for j in i:
        print(j, end=" ")
    print()