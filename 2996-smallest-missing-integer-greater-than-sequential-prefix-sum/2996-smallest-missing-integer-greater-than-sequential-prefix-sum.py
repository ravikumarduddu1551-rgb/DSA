class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i, j = 0, 1
        l = []
        ps = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                ps += nums[i]
            else:
                break
        
        while ps in nums:
            ps += 1
        return ps
