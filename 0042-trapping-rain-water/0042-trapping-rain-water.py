class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        i, j = 0, n-1
        lm = h[0]
        rm = h[-1]
        tot = 0
        while i <= j:
            if lm <= rm:
                if lm - h[i] > 0:
                    tot += lm - h[i]
                lm = max(lm, h[i])
                i += 1
            elif lm > rm:
                if rm - h[j] > 0:
                    tot += rm - h[j]
                rm = max(rm, h[j])
                j -= 1
        return tot


