class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mi = min(edges[0])
        ma = max(edges[0])
        i = 1
        while True:
            if mi in edges[i]:
                return mi
            else:
                return ma
            i += 1