'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        rep=[[root.val]]
        rootlist=[root]
        while rootlist:
            tmp=[]
            len_rootlist=len(rootlist)
            for i in range(len_rootlist):
                curroot=rootlist.pop(0)
                if curroot.left:
                    rootlist.append(curroot.left)
                    tmp.append(curroot.left.val)
                if curroot.right:
                    rootlist.append(curroot.right)
                    tmp.append(curroot.right.val)
            if tmp:
                rep.append(tmp)
        return rep
