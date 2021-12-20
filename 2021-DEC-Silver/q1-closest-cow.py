K, M, N = [int(i) for i in input().split(" ")]

patches = []
nhoj_cows = []

for i in range(K):                              # O(K)
    p_i, t_i = [int(i) for i in input().split(" ")]

    patches.append([p_i, t_i, float("-inf"), float("inf")])

prev = 0
idx = 0

for i in range(M):                              # O(M)
    # cow_pos = int(input())
    # if patches[idx][0] - abs(patches[idx][0] - cow_pos) >= patches[idx][2]:
    #     patches[idx][2] = patches[idx][0] - abs(patches[idx][0] - cow_pos)
    #     patches[idx][3] = patches[idx][0] + abs(patches[idx][0] - cow_pos)

    # else:
    #     idx += 1
    #     patches[idx][2] = patches[idx][0] - abs(patches[idx][0] - prev)
    #     patches[idx][3] = patches[idx][0] + abs(patches[idx][0] - prev)
    # prev = cow_pos
    nhoj_cows.append(int(input()))


def find_nearest_cow(patch_pos:int, cows:list, idx:int):
    diff = float("inf");

    while idx < len(cows) and (abs(patch_pos - cows[idx]) <= diff):
        diff = abs(patch_pos - cows[idx])
        idx += 1

    return [diff, idx - 1]

if __name__ == "__main__":
    idx = 0

    i = 0
    while i < len(patches):                     # O(M+K)
        dist_closest, idx = find_nearest_cow(patches[i][0], nhoj_cows, idx)
        patches[i] = [patches[i][0], patches[i][1], patches[i][0] - dist_closest, patches[i][0] + dist_closest]

        if i != 0 and patches[i][2] < patches[i-1][3]:
            bef = patches[i-1]

            patches[i] = [0, patches[i][1] + bef[1], patches[i][2], bef[3]]
            patches.pop(i-1)
        
        else: i += 1

    patches = sorted(patches, key=lambda x: x[1], reverse=True)

    taste_sum = 0

    for j in range(N):                          #O(N)
        taste_sum += patches[j][1]

    print(taste_sum)

