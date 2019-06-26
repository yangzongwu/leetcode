# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        rep=[]
        self.tree_to_list(root,rep)
        
        left=0
        cur_cnt=0
        result=[]
        while left<len(rep):
            cnt=1
            right=left+1
            while right<len(rep) and rep[right]==rep[left]:
                right+=1
                cnt+=1
            if cnt>cur_cnt:
                result=[rep[left]]
                cur_cnt=cnt
            elif cnt==cur_cnt:
                result.append(rep[left])
                cur_cnt=cnt
            left=right
        return result
        
    def tree_to_list(self,root,rep):
        if not root:
            return        
        self.tree_to_list(root.left,rep)
        rep.append(root.val)
        self.tree_to_list(root.right,rep)
