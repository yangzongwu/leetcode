'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.pathSum(root.left,sum)+self.pathSum(root.right,sum)+self.pathFromRootSum(root,sum)
    
    def pathFromRootSum(self,root,sum):
        if not root:
            return 0
        if sum==root.val:
            return 1+self.pathFromRootSum(root.left,sum-root.val)+self.pathFromRootSum(root.right,sum-root.val)
        return self.pathFromRootSum(root.left,sum-root.val)+self.pathFromRootSum(root.right,sum-root.val)
