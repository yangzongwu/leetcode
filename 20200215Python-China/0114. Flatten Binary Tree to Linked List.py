'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        if root.left:
            rootleft=self.flatten(root.left)
            cur=rootleft
            while cur.right:
                cur=cur.right
            cur.right=self.flatten(root.right)
            root.left=None
            root.right=rootleft
            return root
        else:
            root.right=self.flatten(root.right)
            return root
