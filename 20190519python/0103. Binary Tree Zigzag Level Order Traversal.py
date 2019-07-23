# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        root_stack=[root]
        rep=[]
        flag=True
        while root_stack:
            len_root_stack=len(root_stack)
            tmp=[]
            for k in range(len_root_stack):
                cur_root=root_stack.pop(0)
                tmp.append(cur_root.val)
                if cur_root.left:
                    root_stack.append(cur_root.left)
                if cur_root.right:
                    root_stack.append(cur_root.right)
            if flag==True:
                rep.append(tmp)
                flag=False
            else:
                rep.append(tmp[::-1])
                flag=True
        return rep
                    
