'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        root_list=[root]
        cnt=0
        while root_list:
            cnt+=1
            len_root_list=len(root_list)
            for s in range(len_root_list):
                newroot=root_list.pop(0)
                if  not newroot.left and not newroot.right:
                    return cnt
                else:
                    if newroot.left:
                        root_list.append(newroot.left)
                    if newroot.right:
                        root_list.append(newroot.right)
        return cnt
                                                                                        
