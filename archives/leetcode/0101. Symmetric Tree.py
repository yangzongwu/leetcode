'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root:
            return self.subIsSymmetic(root.left,root.right)
    def subIsSymmetic(self,rootA,rootB):
        if not rootA and not rootB:
            return True
        if rootA and rootB:
            if rootA.val==rootB.val:
                return self.subIsSymmetic(rootA.left,rootB.right) and self.subIsSymmetic(rootA.right,rootB.left)
        return False
#####################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.subIsSymmetrice(root.left,root.right)
        
    def subIsSymmetrice(self,rootA,rootB):
        if not rootA and not rootB:
            return True
        elif (not rootA and rootB) or (rootA and not rootB):
            return False
        else:
            return rootA.val==rootB.val and self.subIsSymmetrice(rootA.left,rootB.right) and self.subIsSymmetrice(rootA.right,rootB.left)
        
