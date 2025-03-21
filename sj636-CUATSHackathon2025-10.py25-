# 36. Valid Sudoku	
# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        j = 0;k = 0
        for i in range(9):
            Check1 = self.ListContainsDuplicates(board[i])
            Columns = [x[i] for x in board]
            Check2 = self.ListContainsDuplicates(Columns)
            
            if j<9:
                Block = board[k][j:j+3]+board[k+1][j:j+3]+board[k+2][j:j+3]
                j=j+3
            else:
                j = 0;k=k+3
                Block = board[k][j:j+3]+board[k+1][j:j+3]+board[k+2][j:j+3]
                j=j+3
            Check3 = self.ListContainsDuplicates(Block)
            if (Check1 == True or Check2 ==True or Check3==True):
                return False
        return True
                
            
        
    
    def ListContainsDuplicates(self,arr):
        arr = [x for x in arr if x!="."]
        if len(set(arr))==len(arr):
            return False
        else:
            return True
        
        
