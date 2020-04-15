'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, 
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left and not root.right:
            return -1
        if root.left:
            if root.val<root.left.val:
                tmpvalueleft=root.left.val
            else:
                tmpvalueleft=self.findSecondMinimumValue(root.left)
        if root.right:
            if root.val<root.right.val:
                tmpvalueright=root.right.val
            else:
                tmpvalueright=self.findSecondMinimumValue(root.right)
        if tmpvalueleft==-1 and tmpvalueright==-1:
            return -1
        elif tmpvalueleft==-1 and tmpvalueright!=-1:
            return tmpvalueright
        elif tmpvalueleft!=-1 and tmpvalueright==-1:
            return tmpvalueleft
        else:
            return min(tmpvalueleft,tmpvalueright)
            
