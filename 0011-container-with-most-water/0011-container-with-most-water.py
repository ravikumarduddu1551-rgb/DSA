class Solution:
    def maxArea(self, h: List[int]) -> int:
        j = len(h)-1
        i = 0
        area = 0
        while i < j:
            w = j - i
            t = w*min(h[i],h[j])
            area = area if area > t else t
            if h[i] < h[j]:
                i += 1
            elif h[i] >= h[j]:
                j -=1
        return area