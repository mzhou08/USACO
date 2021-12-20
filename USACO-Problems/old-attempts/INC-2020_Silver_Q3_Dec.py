N = int(input())

cows = [[] for i in range(N)]

for i in range(N):
    temp = input().split(' ')
    cows[i].append(temp[0])
    tl = []
    tl.append(int(temp[1]))
    tl.append(int(temp[2]))
    cows[i].append(tl)

blame = [0 for i in range(N)]
stopped = []

def move(num, cow: list):
    if num not in stopped:
        dr = cow[0]
        coords = cow[1]
        if coords in '''visited how to keep track of this''':
            blame[num] += 1
            stopped.append(num)
            '''how to make the recursive/transitive stopping?'''

while len(stopped) < N:
    for i in range(len(cows)):
        move(i, cows[i])

grass = {}

for i in range(N):
    print(blame[i])