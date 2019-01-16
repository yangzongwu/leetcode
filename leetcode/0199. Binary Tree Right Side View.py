'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of 
the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            len_rootlist=len(root_list)
            i=0
            while i<len_rootlist:
                cur_root=root_list.pop(0)
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
                i+=1
            rep.append(cur_root.val)
        return rep
