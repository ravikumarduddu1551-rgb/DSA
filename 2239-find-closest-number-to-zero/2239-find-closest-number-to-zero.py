class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float(inf)
        for d in nums:
            if abs(d) < abs(res):
                res = d
            elif abs(d) == abs(res) and d > 0:
                res = d
        return res
