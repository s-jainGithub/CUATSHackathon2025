# 125. Valid Palindrome	
# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r = len(s)-1
        s = s.lower()
        s = ''.join([s_ for s_ in s.lower() if s_.isalnum()])
        if s==s[::-1]:
            return True
        else:
            return False
