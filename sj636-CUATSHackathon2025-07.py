# 242. Valid Anagram	
# https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        T = len(t)
        dict1={}
        dict2={}
        if S!=T:
            return False
        else:
            for i in range(S):
                if s[i] not in dict1:
                    dict1[s[i]]=1
                else:
                    dict1[s[i]]+=1
                if t[i] not in dict2:
                    dict2[t[i]]=1
                else:
                    dict2[t[i]]+=1
        if dict1==dict2:
            return True
        else:
            return False
        
        
