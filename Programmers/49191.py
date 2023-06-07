import copy
from collections import defaultdict


def solution(n, results):
    answer = 0
    windict = defaultdict(set)
    losedict = defaultdict(set)
    
    for win, lose in results:
        windict[win].add(lose)
        losedict[lose].add(win)
    
    for i in range(1, n+1):
        for lose in windict[i]:
            losedict[lose].update(losedict[i])
            
        for win in losedict[i]:
            windict[win].update(windict[i])
        
    for i in range(1, n+1):
        if len(windict[i]) + len(losedict[i]) ==n-1:
            answer+=1
        
        
    return answer