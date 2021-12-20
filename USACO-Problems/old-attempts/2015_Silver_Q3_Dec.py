import time

nq = [int(i) for i in input().split(' ')]
N = nq[0]
Q = nq[1]
ids = []
qs = []

for i in range(N):
    ids.append(int(input()))

for j in range(Q):
    qs.append([int(i) for i in input().split(' ')])

start_time = time.time()

presums = [[0, 0, 0] for i in range(N)]

total = [0, 0, 0]

#presums[0][ids[0] - 1] += 1

for i in range(N):
    #presums[i] = list(presums[i-1])
    #presums[i][ids[i] - 1] += 1
    total[ids[i] - 1] += 1
    presums[i] = list(total)
    #print(presums)

print(presums)

for j in range(Q):
    b1 = 0
    b2 = 0
    b3 = 0
    start = qs[j][0] - 1
    end = qs[j][1] - 1
    b1 = max(presums[end][0], presums[start][0])
    b2 = max(presums[end][1], presums[start][1])
    b3 = max(presums[end][2], presums[start][2])
    print(str(b1) + " " + str(b2) + " " + str(b3))

print(str(time.time() - start_time) + " seconds")