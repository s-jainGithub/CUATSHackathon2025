class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i,j,grid):
            if i>=0 and i<rows and j>=0 and j<cols and grid[i][j]=="1":
                grid[i][j] = "0"
            else:
                return

            dfs(i+1,j,grid)
            dfs(i-1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j,grid)
        return count

            

