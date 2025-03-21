# 53. Maximum Subarray	
# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        #Kadane's Algorithm
        current_sum = 0
        max_sum = nums[0]

        for n in nums:
            current_sum+=n
            if current_sum>max_sum:
                max_sum=current_sum
            if current_sum<0:
                current_sum=0

        return max_sum
        
