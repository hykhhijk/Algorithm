def solution(a):
    answer = 0
    
    first = a[0]
    last = a[-1]
    temp = set()
    for i in range(len(a)):
        if a[i] <= first:
            first = a[i]
            temp.add(a[i])
            
    for i in range(len(a)-1, -1, -1):
        if a[i] <= last:
            last = a[i]
            temp.add(a[i])
    
    
    return len(temp)