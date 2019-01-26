# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            len_root_list=len(root_list)
            tmp=0
            cnt=0
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                cnt+=1.0
                tmp+=cur_root.val
                if cur_root.left:
                    root_list.append(cur_root.left)
                if cur_root.right:
                    root_list.append(cur_root.right)
            rep.append(tmp/cnt)
        return rep
