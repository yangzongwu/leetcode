# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        root=self.remarktree(root)
        root_list=[root]
        rep=0
        while root_list:
            len_root_list=len(root_list)
            for _ in range(len_root_list):
                cur_root=root_list.pop()
                if cur_root.right and cur_root.left:
                    rep=max(rep,cur_root.left.val+cur_root.right.val)
                    root_list.append(cur_root.right)
                    root_list.append(cur_root.left)
                elif not cur_root.right and cur_root.left:
                    rep=max(rep,cur_root.left.val)
                    root_list.append(cur_root.left)
                elif cur_root.right and not cur_root.left:
                    rep=max(rep,cur_root.right.val)
                    root_list.append(cur_root.right)
        return rep
                
        
        
    def remarktree(self,root):
        if not root.left and not root.right:
            root.val=1
        elif not root.left and root.right:
            root.val=1+self.remarktree(root.right).val
        elif root.left and not root.right:
            root.val=1+self.remarktree(root.left).val
        else:
            root.val=1+max(self.remarktree(root.left).val,+self.remarktree(root.right).val)
        return root
