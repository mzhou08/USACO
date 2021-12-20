N = int(input())

coords = {}

for i in range(N):
    c = [int(i) for i in input().split(" ")]
    coords[i] = c

xsort = sorted(coords.items(), key = lambda x: x[1][0])
ysort = sorted(coords.items(), key = lambda x: x[1][1])

def lowsearch(low, ls, xy): #0 for x, 1 for y
    l = 0
    r = N - 1
    ans = []
    while l <= r:
        mid = l + (r - l) // 2
        if ls[mid][1][xy] >= low:
             ans.append(int(ls[mid][0]))
             r = mid
        else:
            l = mid + 1
    return ans

def highsearch(high, ls, xy):
    l = 0
    r = N - 1
    ans = []
    while l <= r:
        mid = l + (r - l) // 2
        if ls[mid][1][xy] <= high:
             ans.append(int(ls[mid][0]))
             l = mid
        else:
            r = mid - 1
    return ans

subsets = []


for i in range(N):
    for j in range(i):
        xh = highsearch(xsort[i][1][0], xsort, 0)
        xl = lowsearch(xsort[j][1][0], xsort, 0)
        subsx = [i for i in xh if i in xl]
        yh = highsearch(max(xsort[i][1][1], xsort[j][1][1]), ysort, 1)
        yl = lowsearch(min(xsort[i][1][1], xsort[j][1][1]), ysort, 1)
        subsx = [i for i in xh if i in xl]
        temp = [i for i in subsx if i in subsy]

        subsets.extend(temp)

print(subsets)


fin = (2 ** N) - len(subsets)

print(fin)