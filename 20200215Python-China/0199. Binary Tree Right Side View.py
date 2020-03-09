'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            len_root_list=len(root_list)
            for k in range(len_root_list):
                cur=root_list.pop(0)
                if k==len_root_list-1:
                    rep.append(cur.val)
                if cur.left:
                    root_list.append(cur.left)
                if cur.right:
                    root_list.append(cur.right)
        return rep
