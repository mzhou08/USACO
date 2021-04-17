nq = input().split(' ')
N = int(nq[0])
Q = int(nq[1])
queries = []
nums = input().split(' ')
nums = [int(i) for i in nums]

print(nums)
for i in range(Q):
    queries.append([int(i) for i in input().split(' ')])

def sumit(start, end):
    count = 0
    for i in range(start, end):
        count  += nums[i]
    return count

for i in range(len(queries)):
    print(sumit(queries[i][0], queries[i][1]))