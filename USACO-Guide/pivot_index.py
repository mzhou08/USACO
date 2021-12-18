class Solution:
    def pivotIndex(self, nums: list(int)):
        total = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i]) == (total - nums[i])/2:
                return i
        return -1