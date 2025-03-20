class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        l=0
        r=N-1
        if nums[0]==target:
            return 0
        if len(nums)==2:
            if nums[1]==target:
                return 1
        while r-l>1:
            m = (r+l)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m
            else:
                r=m
            if nums[m+1]==target:
                return m+1
        return -1
        
