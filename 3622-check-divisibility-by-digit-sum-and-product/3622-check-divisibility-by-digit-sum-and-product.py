class Solution:
    def checkDivisibility(self, n: int) -> bool:
        k = n
        ds, dp = 0, 1
        while k > 0:
            ds += k % 10
            dp *= k % 10 
            k //= 10
        if n % (ds + dp) == 0:
            return True
        else:
            return False