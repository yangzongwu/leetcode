# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        root_list=[root]
        root_list_val=[0]
        dictroottotal={}
        while root_list:
            len_root_list=len(root_list)
            dictlevel={}
            for _ in range(len_root_list):
                
                cur_root=root_list.pop(0)
                cur_loc=root_list_val.pop(0)
                
                if cur_loc not in dictlevel:
                    dictlevel[cur_loc]=[cur_root.val]
                else:
                    dictlevel[cur_loc].append(cur_root.val)
                    
                if cur_root.right:
                    root_list.append(cur_root.right)
                    root_list_val.append(cur_loc+1)
                if cur_root.left:
                    root_list.append(cur_root.left)
                    root_list_val.append(cur_loc-1)      
            for key in dictlevel:
                num=dictlevel[key]
                num.sort()
                print(num)
                if key not in dictroottotal:
                    dictroottotal[key]=num
                else:
                    dictroottotal[key]+=num
            
        rep=[]
        for key in dictroottotal:
            rep.append(key)
        rep.sort()
        res=[]
        for i in rep:
            res.append(dictroottotal[i])
        return res
