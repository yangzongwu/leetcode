'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1_leaf=self.rootToLeaf(root1)
        root2_leaf=self.rootToLeaf(root2)
        if len(root1_leaf)!=len(root2_leaf):
            return False
        for k in range(len(root1_leaf)):
            if root1_leaf[k]!=root2_leaf[k]:
                return False
        return True

    def rootToLeaf(self,root):
        if not root:
            return []
        root_list=[root]
        leaf=[]
        while root_list:
            cur_root=root_list.pop()
            if cur_root.right:
                root_list.append(cur_root.right)
            if cur_root.left:
                root_list.append(cur_root.left)
            if not cur_root.left and not cur_root.right:
                leaf.append(cur_root.val)
        return leaf
