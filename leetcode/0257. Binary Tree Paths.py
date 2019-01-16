'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        rootlist=[root]
        rootlistval=[str(root.val)]
        rep=[]
        while rootlist:
            len_rootlist=len(rootlist)
            cur_root=rootlist.pop(0)
            cur_rootval=rootlistval.pop(0)
            if cur_root.left:
                rootlist.append(cur_root.left)
                rootlistval.append(cur_rootval+'->'+str(cur_root.left.val))
            if cur_root.right:
                rootlist.append(cur_root.right)
                rootlistval.append(cur_rootval+'->'+str(cur_root.right.val))
            if not cur_root.left and not cur_root.right:
                rep.append(cur_rootval)
        return rep
