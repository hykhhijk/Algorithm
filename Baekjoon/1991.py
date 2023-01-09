import sys
sys.setrecursionlimit(10**6)

def bfs(x):
    result.append(x)
    if tree[x][0] != 0:
        bfs(tree[x][0])
    if tree[x][1] != 0:
        bfs(tree[x][1])

def inorder(x):
    if tree[x][0] != 0:
        inorder(tree[x][0])
    result.append(x)
    
    if tree[x][1] != 0:
        inorder(tree[x][1])

def dfs(x):
    if tree[x][0] != 0:
        dfs(tree[x][0])
    if tree[x][1] != 0:
        dfs(tree[x][1])
    result.append(x)

n = int(input())
tree = [[] for _ in range(n+1)]

num_dict={".":0}
for i in range(65, 91):
    num_dict[chr(i)] = i-64
# num_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, ".":0}
char_dict = {v:k for k,v in num_dict.items()}
def convert(x):
    return num_dict[x]
def convert_char(x):
    return char_dict[x]
for _ in range(n):
    temp = list(map(convert, sys.stdin.readline().split()))
    tree[temp[0]].append(temp[1])
    tree[temp[0]].append(temp[2])

result=[]
bfs(1)
for i in range(len(result)):
    print(convert_char(result[i]), end="")
print()
result=[]

inorder(1)
for i in range(len(result)):
    print(convert_char(result[i]), end="")
print()

result= []
dfs(1)
for i in range(len(result)):
    print(convert_char(result[i]), end="")