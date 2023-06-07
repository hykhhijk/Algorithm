import math
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    answer_dict = {"-":0}
    enroll_dict={"-":0}
    cost_dict = {"-":0}
    # answer_dict = {"-":0}
    # enroll_dict={"-":0}
    # cost_dict = {"-":0}
    for i, v in enumerate(enroll):
        enroll_dict[v] = referral[i]
        cost_dict[v] = 0
        answer_dict[v] = 0
    
    for i in range(len(seller)):
        cost_dict[seller[i]] += amount[i]*90
        person = enroll_dict[seller[i]]
        temp_amount = amount[i]*10
        while person != "-" and  temp_amount>=1:
            cost_dict[person] += temp_amount - temp_amount//10
            temp_amount = temp_amount//10
            person = enroll_dict[person]

    # for i in range(len(enroll)-1, -1, -1):
    #     answer_dict[enroll[i]] += cost_dict[enroll[i]]
    #     if answer_dict[enroll[i]] /10<1:
    #         pass
    #     else:
    #         answer_dict[enroll_dict[enroll[i]]] += answer_dict[enroll[i]]//10
    #         answer_dict[enroll[i]]-=answer_dict[enroll[i]]//10
        # print(answer_dict)
    # print(cost_dict)
    for i in cost_dict.values():
        answer.append(i)
    answer.pop(0)
    return answer