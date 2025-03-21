class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search across the rows
        #then binary search across the columns
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = len(matrix)-1
        c = len(matrix[0])



        while r-l>1:
            
            if matrix[l][0]==target or matrix[r][cols-1]==target:
                return True
            else:
                m = (r+l)//2
                if matrix[m][0]==target:
                    return True
                elif matrix[m][0] > target:
                    r=m
                else:
                    l = m
        
        #Now another binary search
        arr = matrix[l] + matrix[r]

        print(l,r)

        l = 0
        r = len(arr)-1
        while r-l>1:
            m=(r+l)//2
            if arr[m] == target:
                return True
            elif arr[m]<target:
                l=m
            else:
                r=m
        if arr[r]==target or arr[l]==target:
            return True
        return False

        
