nm = [int(i) for i in input().split(' ')]
n = nm[0]
m = nm[1]

loc = []
conns = []
neighbors = [[] for i in range(n)]
visited = []
mx = float('-inf')
my = float('-inf')
mnx = float('inf')
mny = float('inf')
mp = float('inf')
maxes = []
master = []

for i in range(n):
    loc.append([int(i) for i in input().split(' ')])
 
for i in range(m):
    conns.append([int(i) for i in input().split(' ')])
    neighbors[conns[-1][0] - 1].append(conns[-1][1] - 1)
    neighbors[conns[-1][1] - 1].append(conns[-1][0] - 1)

def dfs(c):
    global mx
    global my
    global mnx
    global mny
    visited.append(c)
    mx = max(loc[c][0], mx)
    my = max(loc[c][1], my)
    mnx = min(loc[c][0], mnx)
    mny = min(loc[c][1], mny)
    for b in neighbors[c]:
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
        temp = []
        diffx = mx-mnx
        diffy = my-mny
        temp.append(diffx)
        temp.append(diffy)
        maxes.append(temp)
        visited = []
        mx = float('-inf')
        my = float('-inf')
        mnx = float('inf')
        mny = float('inf')

for m in maxes:
    mp = min((2 * (m[0] + m[1])), mp)

print(mp)