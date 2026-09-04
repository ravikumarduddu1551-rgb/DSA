class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mi = [nums[-1]]*n
        for i in range(n-2, -1, -1):
            mi[i] = min(nums[i], mi[i+1])
        ma = 0
        for i in range(n):
            ma = max(ma, nums[i])
            if ma - mi[i] <= k:
                return i
        return -1