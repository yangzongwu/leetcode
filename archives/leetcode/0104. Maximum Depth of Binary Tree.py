'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        root_list=[root]
        cnt=0
        while root_list:
            len_root=len(root_list)
            for s in range(len_root):
                newroot=root_list.pop(0)
                if newroot.left:
                    root_list.append(newroot.left)
                if newroot.right:
                    root_list.append(newroot.right)
            cnt+=1
        return cnt
