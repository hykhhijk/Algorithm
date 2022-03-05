n = input()

result = 0
for i in range(len(n)):
    if n[i] == "A" or n[i] == "B" or n[i] == "C":
        result+=3
    elif n[i] == "D" or n[i] == "E" or n[i] == "F":
        result+=4
    elif n[i] == "G" or n[i] == "H" or n[i] == "I":
        result+=5
    elif n[i] == "J" or n[i] == "K" or n[i] == "L":
        result+=6
    elif n[i] == "M" or n[i] == "N" or n[i] == "O":
        result+=7
    elif n[i] == "P" or n[i] == "Q" or n[i] == "R" or n[i]=="S":
        result+=8
    elif n[i] == "T" or n[i] == "U" or n[i] == "V":
        result+=9
    else:
        result+=10

print(result)


        