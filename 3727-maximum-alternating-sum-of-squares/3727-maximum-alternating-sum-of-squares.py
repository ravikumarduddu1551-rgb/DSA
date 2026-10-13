class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i]**2
        nums.sort()
        i = 0
        k = 0
        j = n - 1
        while i < n and k <= j:
            if i % 2 == 0:
                res += nums[j]
                j -= 1
            else:
                res -= nums[k]
                k += 1
            i += 1
        return res