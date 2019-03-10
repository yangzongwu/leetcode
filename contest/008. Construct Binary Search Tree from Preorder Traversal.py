# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return []
        
        def create_tree(preorder):
            if not preorder:
                return None
            root=TreeNode(preorder[0])
            k=1
            while k<len(preorder):
                if preorder[k]<preorder[0]:
                    k+=1
                else:
                    break

            root.right=create_tree(preorder[k:])
            root.left=create_tree(preorder[1:k])
            return root   
        root=create_tree(preorder)
        
        
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            len_root_list=len(root_list)
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                if cur_root:
                    rep.append(cur_root.val)
                    root_list.append(cur_root.left)
                    root_list.append(cur_root.right)
                else:
                    rep.append(None)
            flag=True
            for s in root_list:
                if s!=None:
                    flag=False
            if flag==True:
                break
        while rep[-1]==None:
            rep.pop()
        return rep
                
