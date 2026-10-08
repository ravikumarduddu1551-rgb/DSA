class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize = None)
        def helper(s,n):
            if s > n:
                return 0
            if s == n:
                return 1
            o = helper(s+1,n)
            t = helper(s+2,n)
            return o + t
        def ways(n):
            return helper(0,n)
        return ways(n)