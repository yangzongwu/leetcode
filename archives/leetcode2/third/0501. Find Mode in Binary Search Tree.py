# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rep=[]
        root_list=[root]
        cnt=0
        max_cnt=0
        target=''
        while root_list:
            cur_root=root_list.pop()
            if not cur_root.left and not cur_root.right:
                if target=='':
                    target=cur_root.val
                    cnt+=1
                else:
                    if target==cur_root.val:
                        cnt+=1
                    else:
                        if cnt>max_cnt:
                            rep=[target]
                            max_cnt=cnt
                        elif cnt==max_cnt:
                            rep.append(target)
                        else:
                            pass
                        target=cur_root.val
                        cnt=1
            else:
                if cur_root.right:
                    root_list.append(cur_root.right)
                root_list.append(TreeNode(cur_root.val))
                if cur_root.left:
                    root_list.append(cur_root.left)
       
        if cnt>max_cnt:
            rep=[target]
        elif cnt==max_cnt:
            rep.append(target)
        return rep
                
