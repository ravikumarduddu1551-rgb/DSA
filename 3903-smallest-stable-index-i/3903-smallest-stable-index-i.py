class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mi = [nums[-1]]*n
        ma = [nums[0]]*n
        for i in range(1, n):
            ma[i] = max(nums[i], ma[i-1])
            mi[n - 1 - i] = min(nums[n - i - 1], mi[n - i])
        for i in range(n):
            if ma[i] - mi[i] <= k:
                return i
        return -1