'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        rep=[]
        root_list=[root]
        root_list_cur=[str(root.val)]
        while root_list:
            cur_root=root_list.pop()
            cur_str=root_list_cur.pop()
            if not cur_root.left and not cur_root.right:
                rep.append(cur_str)
            if cur_root.left:
                root_list.append(cur_root.left)
                root_list_cur.append(cur_str+'->'+str(cur_root.left.val))
            if cur_root.right:
                root_list.append(cur_root.right)
                root_list_cur.append(cur_str+'->'+str(cur_root.right.val))
        return rep
