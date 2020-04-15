'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rep=[]
        rootstack=[root]
        
        while rootstack:
            lenrootstack=len(rootstack)
            for i in range(lenrootstack):
                curroot=rootstack.pop()
                if curroot.left:
                    if curroot.right:
                        rootstack.append(curroot.right)
                        rootstack.append(TreeNode(curroot.val))
                        rootstack.append(curroot.left)
                    else:
                        rootstack.append(TreeNode(curroot.val))
                        rootstack.append(curroot.left)
                else:
                    rep.append(curroot.val)
                    if curroot.right:
                        rootstack.append(curroot.right)
        return rep
