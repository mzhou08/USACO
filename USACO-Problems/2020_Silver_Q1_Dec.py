N = int(input())

roads = []
neighbors = [[] for i in range(N)]
for i in range(N - 1):
    roads.append([(int(j) - 1) for j in input().split(' ')])
    neighbors[roads[-1][0]].append(roads[-1][1])
    neighbors[roads[-1][1]].append(roads[-1][0])

count = 0
#modNs = list(neighbors)
visited = [False for i in range(N)]

def opSpread(f):
    global count
    global visited
    tempn = []
    visited[f] = True
    for n in neighbors[f]:
        if visited[n] == False:
            tempn.append(n)
    if len(tempn) == 0:
        return
    else:
        temp = 0
        num = 1
        while num < len(tempn) + 1:
            num = num * 2
            temp += 1
        count += temp
        for t in tempn:
            count += 1
            visited[t] == True
            opSpread(t)

opSpread(0)
print(count)