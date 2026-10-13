class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i]**2
        nums.sort()
        for i in range(n//2):
            res += nums[n-1-i]
            res -= nums[i]
        if n % 2 == 1:
            res += nums[n//2]
        return res