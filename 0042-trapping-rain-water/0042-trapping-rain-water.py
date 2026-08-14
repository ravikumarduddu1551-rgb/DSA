class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        pm = [0]*n
        sm = [0]*n
        pm[0] = h[0]
        for i in range(1, n):
            pm[i] = max(pm[i-1], h[i])
        sm[n-1] = h[n-1]
        for i in range(n-2, -1, -1):
            sm[i] = max(sm[i+1], h[i])
        tot = 0
        for i in range(n):
            wl = min(pm[i], sm[i])
            if (wl - h[i]) > 0:
                tot += wl - h[i]
        return tot