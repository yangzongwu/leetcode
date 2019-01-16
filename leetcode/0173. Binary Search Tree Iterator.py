'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number 
in the BST when next() is called.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root:
            self.stack=[]
        else:
            self.stack=[]
            rep=[root]
            while rep:
                cur_root=rep.pop()
                if not cur_root.right and not cur_root.left:
                    self.stack.append(cur_root.val)
                else:
                    if cur_root.right:
                        rep.append(cur_root.right)
                    rep.append(TreeNode(cur_root.val))
                    if cur_root.left:
                        rep.append(cur_root.left)
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext:
            return self.stack.pop(0)
        else:
            return []
    
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack!=[]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
