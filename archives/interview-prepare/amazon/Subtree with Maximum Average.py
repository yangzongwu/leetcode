'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
Example
Example 1

Input：
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
Output：11(it's a TreeNode)
Example 2

Input：
     1
   /   \
 -5     11
Output：11(it's a TreeNode)
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.average=0
        self.node =None

    def findSubtree2(self, root):
        # Write your code here
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, \
                    left_size + right_size + 1

        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size

        return sum, size
