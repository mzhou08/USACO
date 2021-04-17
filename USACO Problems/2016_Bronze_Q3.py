N = int(input())
moves = [[] for i in range(N)]
loc = [0,0]
visited = []
time = 0
timeReq = -1
noRep = True

for i in range(N):
    moves[i] = input().split(' ')

print(moves)

def move(dir, len):
    global time
    for i in range(int(len)):
        visited.append([loc[0], loc[1], time])
        time +=1
        if dir == 'N': 
            loc[1] +=1
        elif dir == 'S':
            loc[1] -=1
        elif dir == 'E':
            loc[0] +=1
        elif dir == 'W':
            loc[0] -=1

for i in range(N):
    move(moves[i][0], moves[i][1])

print(time)

for i in range(time):
    for j in range(time):
        if visited[i][0] == visited[j][0] and visited[i][1] == visited[j][1] and i!=j:
            tempTime = abs(visited[i][2] - visited[j][2])
            if timeReq == -1:
                timeReq = tempTime
                continue
            else:
                timeReq = min(timeReq, tempTime)
            noRep = False

print("-1" if noRep else timeReq)