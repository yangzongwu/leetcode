'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        root_list=[root]
        rep=[[root.val]]
        while len(root_list)>0:
            tmp=[]
            len_root=len(root_list)
            for s in range(len_root):
                newroot=root_list.pop(0)
                if newroot.left:
                    root_list.append(newroot.left)
                    tmp.append(newroot.left.val)
                if newroot.right:
                    root_list.append(newroot.right)
                    tmp.append(newroot.right.val)
            rep.append(tmp)
        return rep[::-1][1:]

#############################################33
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        rootlist=[root]
        rep=[]
        while rootlist:
            cur=[]
            len_rootlist=len(rootlist)
            for k in range(len_rootlist):
                curroot=rootlist.pop(0)
                cur.append(curroot.val)
                if curroot.left:
                    rootlist.append(curroot.left)
                if curroot.right:
                    rootlist.append(curroot.right)
            rep.append(cur)
        return rep[::-1]
        
        
