class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = 0
        res = float('-inf')
        for d in nums:
            if d<0:
                res = max(res, d)
                c += 1
        if c == len(nums):
            return res
        ms = 0
        cs = 0
        for i in range(len(nums)):
            cs = max(nums[i], cs + nums[i])
            ms = max(ms, cs)
        return ms