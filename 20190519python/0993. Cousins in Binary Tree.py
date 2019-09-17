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
        x_rep=self.getHeight(root,x)
        y_rep=self.getHeight(root,y)
        return x_rep[0]!=y_rep[0] and x_rep[1]==y_rep[1]
    
    def getHeight(self,root,x):
        root_stack=[root]
        cnt=0
        while root_stack:
            len_root_stack=len(root_stack)
            cnt+=1
            for k in range(len_root_stack):
                cur_root=root_stack.pop(0)
                if cur_root.left:
                    if cur_root.left.val==x:
                        return [cur_root,cnt]
                    root_stack.append(cur_root.left)
                if cur_root.right:
                    if cur_root.right.val==x:
                        return [cur_root,cnt]
                    root_stack.append(cur_root.right)
