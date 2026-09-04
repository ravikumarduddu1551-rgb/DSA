class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        return [a.index(nums[i]) for i in range(len(nums))]