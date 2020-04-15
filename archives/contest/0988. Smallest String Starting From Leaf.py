# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        if not root:
            return ''
        
        rep=[]
        root_stack=[root]
        repstr=[[root.val]]
        while root_stack:
            len_root_stack=len(root_stack)
            for _ in range(len_root_stack):
                cur_root=root_stack.pop(0)
                cur_str=repstr.pop(0)
                if not cur_root.left and not cur_root.right:
                    rep=self.cmp(rep,cur_str)
                else:
                    if cur_root.left:
                        root_stack.append(cur_root.left)
                        repstr.append(cur_str+[cur_root.left.val])
                    if cur_root.right:
                        root_stack.append(cur_root.right)
                        repstr.append(cur_str+[cur_root.right.val])
        print(rep)
        ss='abcdefghijklmnopqrstuvwxyz'
        result=''
        for k in rep[::-1]:
            result=result+ss[k]
        return result
    
    def cmp(self,str1,str2):
        if len(str1)==0:
            return str2
        str1=str1[::-1]
        str2=str2[::-1]
        for k in range(len(str1)):
            if k>=len(str2):
                return str2[::-1]
            elif int(str1[k])<int(str2[k]):
                return str1[::-1]
            elif int(str1[k])>int(str2[k]):
                return str2[::-1]
        return str1[::-1]
            
