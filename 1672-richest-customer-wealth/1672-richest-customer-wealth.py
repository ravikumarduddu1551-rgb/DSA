class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mw = 0
        for c in accounts:
            mw = max(mw, sum(c))
        return mw