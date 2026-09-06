class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            s = 0
            x = 1
            for d in weights:
                if s + d > mid:
                    x += 1
                    s = 0
                s += d
            if x <= days:
                r = mid
            else:
                l = mid + 1
        return l