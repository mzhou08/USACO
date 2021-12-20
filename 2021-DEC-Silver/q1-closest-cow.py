K, M, N = [int(i) for i in input().split(" ")]

patches = []
nhoj_cows =[]

for i in range(K):
    p_i, t_i = [int(i) for i in input().split(" ")]

    patches.append([p_i, t_i])

for i in range(M):
    nhoj_cows.append(int(input()))

def find_nearest_cow(patch_pos:int, cows:list, idx:int):
    diff = float("inf");

    while idx < len(cows) and (abs(patch_pos - cows[idx]) <= diff):
        diff = abs(patch_pos - cows[idx])
        idx += 1

    return [diff, idx - 1]

if __name__ == "__main__":
    idx = 0

    intervals = []

    for i in range(len(patches)):
        dist_closest, idx = find_nearest_cow(patches[i][0], nhoj_cows, idx)
        intervals.append([patches[i][1], patches[i][0] - dist_closest, patches[i][0] + dist_closest])

        if i != 0 and intervals[-1][1] < intervals[-2][2]:
            last = intervals.pop()
            sec_last = intervals.pop()

            new_interval = [last[0] + sec_last[0], sec_last[1], sec_last[2]]
            intervals.append(new_interval)

    intervals = sorted(intervals, key=lambda x: x[0], reverse=True)

    taste_sum = 0

    for j in range(N):
        taste_sum += intervals[j][0]

    print(taste_sum)

