from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    hash = defaultdict(int)
    for i in range(len(note1)):
        hash[note1[i]] = 1

    for i in range(len(note2)):
        if hash[note2[i]]==1:
            print("1")
        else:
            print("0")