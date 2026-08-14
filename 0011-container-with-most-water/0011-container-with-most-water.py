class Solution:
    def maxArea(self, h: List[int]) -> int:
        j = len(h)-1
        i = 0
        area = 0
        while i < j:
            w = abs(i - j)
            area = max(area, w*min(h[i],h[j]))
            if h[i] < h[j]:
                i += 1
            elif h[i] > h[j]:
                j -=1
            else:
                i += 1
                j -= 1
        return area

                
            
