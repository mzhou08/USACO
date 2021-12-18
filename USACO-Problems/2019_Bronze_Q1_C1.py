kn = [int(i) for i in input().split(' ')]
K = kn[0]
N = kn[1]
cows = [(i +1) for i in range(N)]
scores = []
con = [[0 for j in range(i)] for i in range(N)]
print(con)
pairs = 0

for i in range(K):
    scores.append([int(i) for i in input().split(' ')])

print(scores)

'''something wrong here'''

for i in range(N):
    #count = 0
    for j in range(i):
        for k in range(K):
            if scores[k].index(i + 1) < scores[k].index(j + 1):
                con[i][j] += 1
                if con[i][j] == K:
                    pairs += 1
                    print(str(i) + " " + str(j))

print(str(pairs))