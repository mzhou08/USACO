nq = [int(i) for i in input().split(' ')]
n = nq[0]
q = nq[1]

s = [int(i) for i in input().split(' ')]

quers = []

for i in range(q):
    quers.append([int(i) for i in input().split(' ')])

bales = sorted(s)

def search(point, bales):
    l = 0
    r = n - 1
    ans = -1

    while l != r:
        mid = (l + r + 1) // 2
        #print(str(l) + " " + str(r) + " " + str(mid))
        if bales[mid] <= point:
            l = mid
            ans = int(mid)
        else:
            r = mid - 1
    return ans


for q in quers:
    templ = search(q[0] - 1, bales)
    tempr = search(q[1], bales)
    print(tempr - templ)