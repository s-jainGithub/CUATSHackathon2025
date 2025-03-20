class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        previous = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in previous:
                return [i,previous[diff]]
            else:
                previous[n] = i
                
