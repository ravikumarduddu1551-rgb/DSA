class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n,k):
            if n == 1:
                return 0
            parent = helper(n-1, (k + 1)//2)
            if k % 2 == 0:
                return 1 - parent
            else:
                return parent
        return helper(n,k)