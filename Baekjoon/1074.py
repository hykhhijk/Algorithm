n, r, c = map(int, input().split())

mat = [[0 for _ in range(2**n)] for _ in range(2**n)]

def recursive(level, row, col, num):

    if level==0:
        mat[row][col] = num
        return mat[row][col]+1
    else:
        value = recursive(level-1, row, col, num)
        value = recursive(level-1, row, col + 2**(level-1), value)
        value = recursive(level-1, row  + 2**(level-1), col, value)
        value = recursive(level-1, row  + 2**(level-1), col + 2**(level-1), value)
        return value


def recursive2(level, row, col, num):
    if level ==-1:
        return num
    
    dist = 2**(level)
    value = dist**2

    if row <dist and col <dist:
        num = recursive2(level-1, row, col, num)
    elif row < dist and col >= dist:
        num += value
        num = recursive2(level-1, row, col - dist, num)
    elif row >= dist and col < dist:
        num += 2 * value
        num = recursive2(level-1, row - dist, col, num)
    else:
        num += 3 * value
        num = recursive2(level-1, row - dist, col - dist, num)
    
    return num



# recursive(n, 0, 0, 0)
# print(mat[r][c])

answer = recursive2(n-1, r, c, 0)
print(answer)