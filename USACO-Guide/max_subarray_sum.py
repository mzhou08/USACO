N = int(input())
nums = [int(i) for i in input().split(' ')]
presums = []
total = 0

for i in nums:
    total = total + i
    presums.append(int(total))

m = presums[0]
mx = presums[0]
mn = presums[-1]

#fast = []

#[fast.append(x) for x in presums if x not in fast]

for i in presums:
    #temp = max(presums[(i+1):])
    if i < mn and presums.index(i) <= presums.index(mx):
        mn = i
    if i > mx:
        mx = i

print(max(mx - mn, mx))