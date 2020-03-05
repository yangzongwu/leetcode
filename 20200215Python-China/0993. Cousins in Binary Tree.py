'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val==x or root.val==y:
            return False

        root_list=[root]
        while root_list:
            len_root_list=len(root_list)
            next_dict={}
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                if cur_root.left:
                    root_list.append(cur_root.left)
                    next_dict[cur_root.left.val]=cur_root.val
                if cur_root.right:
                    root_list.append(cur_root.right)
                    next_dict[cur_root.right.val]=cur_root.val
            if x in next_dict and y not in next_dict:
                return False
            elif x not in next_dict and y in next_dict:
                return False
            elif x in next_dict and y in next_dict:
                return next_dict[x]!=next_dict[y]
        return False
            
