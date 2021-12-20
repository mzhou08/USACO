import itertools

N = int(input())

weights = []

sets = []

for i in range(2^N):

splitW = []

for i in range (N):
    weights.append(int(input()))

maxDigits = 0
for i in range (N):
    splitW[i] = [int(char) for char in str(weights[i])]
    if len(splitW[i]) > maxDigits:
        maxDigits = len(splitW[i])

for i in range(N):
    if len(splitW[i]) < maxDigits:
        for j in range(len(splitW[i]), maxDigits):
            splitW[i].insert(0,0)
        
pairs = list(combinations(weights, 2))

for i in range(len(pairs)):
    sum = pairs[i][0] + pairs[i][1]


#for i in range (N):
#    for j in range (len(W[i]):