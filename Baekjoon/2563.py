import sys

n = int(input())
papers = []
for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().split())))
mat = [[0]*(101) for _ in range(101)]


for i in range(len(papers)):
    paper = papers[i]
    for j in range(10):
        for k in range(10):
            mat[paper[0]+j][paper[1]+k]=1

result = 0
for i in mat:
    result+= sum(i)
print(result)