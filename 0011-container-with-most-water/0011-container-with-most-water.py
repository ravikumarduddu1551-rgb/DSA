class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height)-1
        i = 0
        lm = height[i]
        rm = height[-1]
        area = 0
        while i < j:
            if lm < rm:
                area = max(lm*(j-i), area)
                i += 1
                lm = height[i]
            elif lm == rm:
                area = max(rm*(j-i), area)
                j -= 1
                i += 1
                lm, rm = height[i], height[j]
            else:
                area = max(rm*(j-i), area)
                j -= 1
                rm = height[j]
        return area

                
            
