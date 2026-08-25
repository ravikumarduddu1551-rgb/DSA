class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while k * i in set(nums):
            i += 1
        return k * i
