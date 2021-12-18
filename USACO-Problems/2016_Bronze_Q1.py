divs = [[] for i in range(4)]

for i in range(4):
    divs[i] = input().split(' ')
    divs[i] = list(map(int, divs[i]))


promotions = [0 for i in range(4)]

for i in range(4):
    if divs[i][1]-divs[i][0] <= 0:
        continue
    else:
        for k in range(i):
            promotions[k] = promotions[k] + (divs[i][1]-divs[i][0])
        
print(divs)
print(f"{promotions[0]} \n{promotions[1]} \n{promotions[2]}")