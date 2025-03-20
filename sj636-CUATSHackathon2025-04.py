# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        while p and q:

            if p.val==q.val:
                if p.left ==None and p.right==None and q.right==None and q.left==None:
                    return True
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
        
