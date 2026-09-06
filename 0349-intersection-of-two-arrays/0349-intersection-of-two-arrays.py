class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [d for d in set(nums1) if d in nums2]