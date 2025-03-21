# 695. Max Area of Island	
# https://leetcode.com/problems/max-area-of-island

class Solution:
    count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Depth First Search
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j,grid):
            if i>=0 and i<rows and j>=0 and j<cols and grid[i][j]==1:
                Solution.count+=1
                grid[i][j] = 0
            else:
                return

            dfs(i+1,j,grid)
            dfs(i-1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    Solution.count = 0
                    dfs(i,j,grid)

                    max_area = max(Solution.count,max_area)
        return max_area
