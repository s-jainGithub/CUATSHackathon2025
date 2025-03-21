# 153. Find Minimum in Rotated Sorted Array 
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
class Solution:
    def findMin(self, nums: List[int]) -> int:

        #Need to find the right criteria for shifting the right pointer or left pointer
        N=len(nums)
        l = 0
        r = N-1
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1]:
            return nums[0]
        if nums[-1]<nums[-2]:
            return nums[-1]

        while r-l>1:
            print(l,r)
            m = (r+l)//2
            if nums[m]<nums[l]:
                r = m
            else:
                l=m
        if nums[r]>nums[l]:
            return nums[l]
        else:
            return nums[r]
            
