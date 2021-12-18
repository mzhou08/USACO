nm = [int(i) for i in input().split(' ')]
n = nm[0]
m = nm[1]

roads = []
#visited = [False for i in range(n)]
visited = []
neighbors = [[] for i in range(n)]
master = []


for i in range(m):
    roads.append([int(i) - 1 for i in input().split(' ')])

for r in roads:
    for c in range(n):
        if r[0] == c:
            neighbors[c].append(r[1])
        if r[1] == c:
            neighbors[c].append(r[0])

def dfs(c):
    #visited[c] = True
    visited.append(c)
    for n in neighbors[c]:
        if n not in visited:
            dfs(n)

for i in range(n):
    temp = True
    for j in master:
        if i in j:
            temp = False
    if temp:
        visited = []
        dfs(i)
        master.append(visited)

print(len(master) - 1)

for i in range(len(master) - 1):
    print(str(master[i][0] + 1) + " " + str(master[i + 1][0] + 1))