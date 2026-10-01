class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        # p1, p2 = 0, 0
        # turn = 1
        # while len(nums) > 3:
        #     if nums[1] > nums[-2]:
        #         m = -2
        #     else:
        #         m = 1
        #     if turn:
        #         p1 += nums[m]
        #         nums.pop(m)
        #         turn = 0
        #     elif not turn:
        #         p2 += nums[m]
        #         nums.pop(m)
        #         turn = 1
        # m = 0
        # if nums[0] > nums[-1]:
        #     m = nums[0]
        # else:
        #     m = nums[-1]
        # if turn:
        #     p1 += m
        #     nums.remove(m)
        #     turn = 0
        # elif not turn:
        #     p2 += m
        #     nums.remove(m)
        #     turn = 1
        # if turn:
        #     p1 += nums[-1]
        # else:
        #     p2 += nums[-1]
        # if p1 >= p2:
        #     return True
        # else:
        #     return False
        def helper(l, r):
            if l == r:
                return nums[l]
            left = nums[l] - helper(l+1, r)
            right = nums[r] - helper(l, r-1)
            return max(left, right)
        return helper(0, len(nums) - 1) >= 0