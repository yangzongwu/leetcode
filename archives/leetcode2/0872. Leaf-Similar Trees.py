# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        root1_leaf=self.leaf_root(root1)
        root2_leaf=self.leaf_root(root2)
        return root1_leaf==root2_leaf
    
    def leaf_root(self,root):
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            cur_root=root_list.pop()
            if not cur_root.left and not cur_root.right:
                rep.append(cur_root.val)
            else:
                if cur_root.right:
                    root_list.append(cur_root.right)
                if cur_root.left:
                    root_list.append(cur_root.left)
        return rep
        
