N = int(input())
pos = []
exploded = set()

most = 0
time = 0

for i in range(N):
    pos.append(int(input()))

def explode(start, tRad, exploded):
    exploded.add(pos[start])
    for i in range(N):
        if ((pos[start]-tRad <= pos[start]) or (pos[start] <= pos[start] + tRad)) and (pos[start] not in exploded) and (tRad < N):
            explode(i, tRad + 1, exploded)


for i in range(N):
    exploded = set()
    explode(i, 1, exploded)
    print(exploded)
    most = max(most, len(exploded))

print(most)

'''
C:\Users\Michael\AppData\Local\Programs\Python\Python39\Scripts\

for i in range(N): #scan through all positions
    exploded = []
    exploded.append(pos[i])
    count = 1
    time = 1

    for j in range(N): #scan through all differences to either side
        for k in range(N): #seeing if bales lie inside the intervals
            if pos[k] in exploded:
                continue
            else:
                if ((pos[i]-(j*(j+1)/2) <= pos[k] <= pos[i]-(j*(j-1)/2)) or (pos[i]+(j*(j-1)/2) <= pos[k] <= pos[i]+(j*(j+1)/2))):
                    exploded.append(pos[k])
                    count+=1 
                    most = max(count, most)'''