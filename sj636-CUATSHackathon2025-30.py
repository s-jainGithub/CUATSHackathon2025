# 994. Rotting Oranges	
# https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        k = complex(0,1)
        rows = len(grid)
        cols = len(grid[0])
        
        fresh_oranges = {}
        rotten_oranges = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh_oranges[complex(i,j)] = 1
                elif grid[i][j]==2:
                    rotten_oranges[complex(i,j)] =1
                    
        for minutes in range(rows*cols):
            
            if fresh_oranges=={}:
                return minutes
            new_rotten_oranges = {}
            for ro in rotten_oranges:
                
                if ro+1 in fresh_oranges:
                    new_rotten_oranges[ro+1] = 1
                    fresh_oranges.pop(ro+1)
                    
                    
                if ro-1 in fresh_oranges:
                    new_rotten_oranges[ro-1] = 1
                    fresh_oranges.pop(ro-1)
                    print("UP")
                
                if ro+k in fresh_oranges:
                    new_rotten_oranges[ro+k] = 1
                    fresh_oranges.pop(ro+k)
                    
                if ro-k in fresh_oranges:
                    new_rotten_oranges[ro-k] = 1
                    fresh_oranges.pop(ro-k)
                    
            rotten_oranges = new_rotten_oranges
 

        return -1
            
            
