'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        root_list=[root]
        rootval_list=[root.val]
        sumrep=0
        while root_list:
            len_root_list=len(root_list)
            i=0
            while i<len_root_list:
                cur_root=root_list.pop(0)
                cur_rootval=rootval_list.pop(0)
                if not cur_root.right and not cur_root.left:
                    sumrep+=cur_rootval
                else:
                    if cur_root.right:
                        root_list.append(cur_root.right)
                        rootval_list.append(cur_rootval*10+cur_root.right.val)
                    if cur_root.left:
                        root_list.append(cur_root.left)
                        rootval_list.append(cur_rootval*10+cur_root.left.val)
                i+=1
        return sumrep
