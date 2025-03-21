# 217. Contains Duplicate	
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_={}
        for n in nums:
            if n in dict_:
                return True
            else:
                dict_[n] =1
        return False
        
