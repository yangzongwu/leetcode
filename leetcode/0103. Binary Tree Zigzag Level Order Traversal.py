'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        rep=[[root.val]]
        rootlist=[root]
        flag=0
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
                if flag%2==0:
                    rep.append(tmp[::-1])
                else:
                    rep.append(tmp)
                flag+=1
        return rep
