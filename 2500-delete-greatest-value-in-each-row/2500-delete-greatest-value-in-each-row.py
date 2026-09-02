class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ma = []
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = -grid[i][j]

        for row in grid:
            heapq.heapify(row)

        for _ in range(len(grid[0])):
            for row in grid:
                x = heapq.heappop(row)
                ma.append(x)
            ans -= min(ma)
            ma = []

        return ans