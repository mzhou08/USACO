nq = [int(i) for i in input().split(' ')]
N = nq[0]
Q = nq[1]

trees = [[]for i in range(N)]
coords = []

for i in range(N):
    for char in input():
        temp = 1 if char == '*' else 0
        trees[i].append(temp)

for i in range(Q):
    coords.append([int(i) for i in input().split(' ')])


presums = [[0 for i in range(N)] for i in range(N)]

for y in range(N):
    presums[y][0] = trees[y][0] + presums[y - 1][0]
    presums[0][y] = trees[0][y] + presums[0][y -1]

for y in range(1, N):
    for x in range(1, N):
        presums[y][x] = trees[y][x] + presums[y][x - 1] + presums[y - 1][x] - presums[y-1][x-1]

sols = []

'''
need to add a upper diagonal row + col of 0's to account for -1's.
'''

for q in coords:
    temp = list(map(lambda x: x - 1, q))
    answer = presums[temp[2]][temp[3]] - presums[temp[0] - 1][temp[3]] - presums[temp[2]][temp[1] - 1] + presums[temp[0] - 1][temp[1] - 1]
    sols.append(answer)

print(sols)