class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isSameTree(s,t):
            return True
        elif not s:
            return False
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def isSameTree(self,s,t):
        if not s and not t:
            return True
        elif not s and t:
            return False
        elif s and not t:
            return False
        else:
            return s.val==t.val and self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
