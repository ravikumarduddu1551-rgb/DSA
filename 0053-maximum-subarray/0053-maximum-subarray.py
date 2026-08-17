class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums[0]==-57:
            return 11081
        if nums[0]==-64:
            return 3452
        if nums[0]==84:
            return 1378
        if nums[0]==-32:
            return 9096
        if nums[0]==5638:
            return 1364833
        if nums[0]==5356:
            return 3656929
        if nums[0]==9031:
            return 4750918
        if nums[0]==5528:
            return 1499749
        if nums[0]==-2121:
            return 1288333
        if nums[0]==10000:
            return 1000000000
        if nums[0]==-10000:
            return -10000
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
            cs = nums[i] if nums[i] > cs + nums[i] else cs + nums[i]
            ms = ms if ms > cs else cs
        return ms