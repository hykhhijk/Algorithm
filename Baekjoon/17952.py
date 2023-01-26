import sys

N = int(input())
projects = []
for _ in range(N):
    projects.append(list(map(int, sys.stdin.readline().split())))

ongoings = []
score = 0
for i in range(len(projects)):
    project = projects[i]
    if ongoings:
        ongoing = ongoings[-1]
        if ongoing[1]-1==0:
            score += ongoing[0]
            ongoings.pop()
        else:
            ongoings[-1][1] -=1
    if project[0]==1:
        ongoings.append(project[1:])
    else:
        continue
if ongoings:
        ongoing = ongoings[-1]
        if ongoing[1]-1==0:
            score += ongoing[0]
            ongoings.pop()
print(score)
