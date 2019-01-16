'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter 
of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.revalueTree(root)
        listroot=[root]
        rep=0
        while listroot:
            len_listroot=len(listroot)
            for i in range(len_listroot):
                curroot=listroot.pop(0)
                if curroot.left:
                    listroot.append(curroot.left)
                if curroot.right:
                    listroot.append(curroot.right)
                if curroot.left and curroot.right:
                    rep=max(rep,curroot.val+min(curroot.right.val,curroot.left.val))
                else:
                    rep=max(rep,curroot.val)
        return rep-1
        
        
    def revalueTree(self,root):
        if not root:
            return 0
        root.val=1+max(self.revalueTree(root.left),self.revalueTree(root.right))
        return root.val
