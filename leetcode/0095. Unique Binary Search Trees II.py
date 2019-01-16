'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        listn=[i for i in range(1,n+1)]
        return self.subGenerateTree(listn)

    def subGenerateTree(self,listn):
        if not listn:
            return [None]
        rep=[]
        for i in range(len(listn)):
            left=self.subGenerateTree(listn[:i])
            right=self.subGenerateTree(listn[i+1:])
            
            for lefttree in left:
                for righttree in right:
                    newtree=TreeNode(listn[i])
                    newtree.left=lefttree
                    newtree.right=righttree
                    rep.append(newtree)
        return rep
