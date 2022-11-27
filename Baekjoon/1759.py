import itertools

vowel=["a","e","i","o","u"]
n,m = map(int, input().split())
str_list = input().split()
str_list.sort()
combinations = itertools.combinations(str_list, n)
combinations = list(combinations)


for password in combinations:
    countv = 0
    countc = 0
    for j in password:
        if j in vowel:
            countv +=1
        else:
            countc+=1
    if countv>=1 and countc>=2:
        print("".join(password))