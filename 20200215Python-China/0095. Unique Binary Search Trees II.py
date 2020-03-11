'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        rep=[x for x in range(1,n+1)]
        return self.generateTreesFromList(rep)


    def generateTreesFromList(self,listn):
        if not listn:
            return [None]
        rep=[]
        for k in range(len(listn)):
            rootleft=self.generateTreesFromList(listn[:k])
            rootright=self.generateTreesFromList(listn[k+1:])
            for l in rootleft:
                for r in rootright:
                    root=TreeNode(listn[k])
                    root.left=l
                    root.right=r
                    rep.append(root)
        return rep
        

