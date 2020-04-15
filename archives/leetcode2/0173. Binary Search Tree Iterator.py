# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.len=0
        self.stack=[]
        self.cur=0
        
        if root:
            rootlist=[]
            while root or rootlist:
                while root:
                    rootlist.append(root)
                    root=root.left
                cur_root=rootlist.pop()
                self.stack.append(cur_root.val)
                
                root=cur_root.right
                self.len+=1
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext:
            self.cur+=1
            return self.stack[self.cur-1]
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.cur<self.len


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
