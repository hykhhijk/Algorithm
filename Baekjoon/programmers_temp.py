import re
# import pandas as pd

def solution(info, query):
    answer = []    
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    info = str(info).split(",")
    participant= []
    for i in info:
        # re.findall(r"[a-z0-9]* [a-z0-9]* [a-z0-9]* [a-z0-9]* [a-z0-9]*", i)[0].split()
        participant.append(re.findall(r"[a-z0-9]* [a-z0-9]* [a-z0-9]* [a-z0-9]* [a-z0-9]*", i)[0].split())
    # for j in participant:
        # print(j)
    # temp = pd.DataFrame(participant)





    return answer


solution(0, 0)