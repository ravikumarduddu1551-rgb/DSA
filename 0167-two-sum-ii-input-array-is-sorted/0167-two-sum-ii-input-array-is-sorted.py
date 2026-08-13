class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k in range(len(nums) - 1):
            l = k + 1
            r = len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[k] + nums[mid] == target:
                    return [k+1, mid+1]
                elif nums[k] + nums[mid] < target:
                    l = mid + 1
                    mid = (l + r)//2 
                else:
                    r = mid - 1
                    mid = (l + r)//2
    