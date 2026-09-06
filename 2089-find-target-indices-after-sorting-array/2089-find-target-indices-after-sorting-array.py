class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = []
        while l <= r:
            if nums[l] == target:
                ans.append(l)
                l += 1
            elif nums[r] == target:
                ans.append(r)
                r -= 1
            else:
                l += 1
                r -= 1
        return sorted(ans)