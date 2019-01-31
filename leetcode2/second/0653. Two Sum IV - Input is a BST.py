class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        rep=[]
        self.treeToList(root,rep)
        
        left=0
        right=len(rep)-1
        
        while right>left:
            if rep[right]+rep[left]==k:
                return True
            elif rep[right]+rep[left]>k:
                right-=1
            else:
                left+=1
        return False
    
    def treeToList(self,root,rep):
        if not root:
            return
        if root.left:
            self.treeToList(root.left,rep)
        rep.append(root.val)
        if root.right:
            self.treeToList(root.right,rep)
        
