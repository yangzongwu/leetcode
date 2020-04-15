# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        self.readTree(root)
        
    def readTree(self,root):
        if not root:
            return
        if root.left:
            self.readTree(root.left)
        self.stack.append(root.val)
        if root.right:
            self.readTree(root.right)
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop(0)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
