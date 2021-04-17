nm = [int(i) for i in input().split(' ')]
n = nm[0]
m = nm[1]

ships = []
fs = [[] for i in range(n)]
visited = {}
master = []
 
for i in range(m):
    ships.append([int(i) for i in input().split(' ')])
    fs[ships[-1][0] - 1].append(ships[-1][1] - 1)
    fs[ships[-1][1] - 1].append(ships[-1][0] - 1)

def dfs(c):
    '''figure out how to check for equality to previous entry'''
    visited[c] = 1
    for b in fs[c]:
        if b not in visited:
            dfs(b)

for i in range(n):
    t = True
    for j in master:
        if i in j:
            t = False
    if t:
        dfs(i)
        master.append(visited)
        visited = []