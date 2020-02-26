'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        root_list=[]
        self.treeToList(root,root_list)
        
        rep=[]
        rep_cnt=0
        k=0
        while k<len(root_list):
            target=root_list[k]
            cnt=1
            k+=1
            while k<len(root_list) and root_list[k]==target:
                k+=1
                cnt+=1
            if cnt>rep_cnt:
                rep=[target]
                rep_cnt=cnt
            elif cnt==rep_cnt:
                rep.append(target)
        return rep


    def treeToList(self,root,rep):
        if not root:
            return
        self.treeToList(root.left,rep)
        rep.append(root.val)
        self.treeToList(root.right,rep)
