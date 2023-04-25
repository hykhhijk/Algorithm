def solution(gems):
    answer = [100001, 100001]
    start=0
    end=0
    maxg = len(set(gems))
    dictg = {}
    dictg[gems[start]]=1
    cnt=0
    while True:
        if len(dictg) < maxg:
            cnt+=1
            end+=1
            if end==len(gems):
                break
            if dictg.get(gems[end])==None:
                dictg[gems[end]]=1
            else:
                dictg[gems[end]]+=1
        else:
            if  dictg[gems[start]]==1:
                del dictg[gems[start]]
            else:
                dictg[gems[start]]-=1
            gems[start]=cnt
            if cnt < answer[1]:
                answer = [start, cnt]
            cnt-=1
            start+=1
            if start > end:
                break
            
    return answer[0]+1, answer[0]+answer[1]+1