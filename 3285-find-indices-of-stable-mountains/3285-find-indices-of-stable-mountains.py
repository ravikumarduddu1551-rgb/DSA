class Solution:
    def stableMountains(self, h: List[int], t: int) -> List[int]:
        return [i for i in range(1, len(h)) if h[i-1] > t]    