def solution(sticker):
    answer = 0
    if len(sticker)==1:
        return sticker[0]
    
    mat = [0 for _ in range(len(sticker))]

    mat[0] = sticker[0]
    mat[1] = sticker[0]
        
    for i in range(2, len(sticker)-1):
        mat[i] = max(mat[i-1], sticker[i]+mat[i-2])
    value = mat[-2]
    
    
    mat = [0 for _ in range(len(sticker))]
    mat[0] = 0
    mat[1] = sticker[1]
        
    for i in range(2, len(sticker)):
        mat[i] = max(mat[i-1], sticker[i]+mat[i-2])
        
    return max(value, mat[-1])