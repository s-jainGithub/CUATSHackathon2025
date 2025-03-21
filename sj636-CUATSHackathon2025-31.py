# 130. Surrounded Regions	
# https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Need to look at the edges of the board
                #Depth First Search
        rows = len(board)
        cols = len(board[0])

        def dfs(i,j,board):
            if i>=0 and i<rows and j>=0 and j<cols and board[i][j]=="O":
                board[i][j] = "*"
            else:
                return

            dfs(i+1,j,board)
            dfs(i-1,j,board)
            dfs(i,j+1,board)
            dfs(i,j-1,board)

        #Depth first search on the edges
        for j in range(cols):
            dfs(0,j,board)
            dfs(rows-1,j,board)
        for i in range(rows):
            dfs(i,0,board)
            dfs(i,cols-1,board)

        #Now replace "O" with "X" and "*" with "O"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"
