# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        rep=[]
        root_list=[root]
        root_parth=[str(root.val)]
        while root_list:
            len_root_list=len(root_list)
            for _ in range(len_root_list):
                cur_root=root_list.pop(0)
                cur_path=root_parth.pop(0)
                if not cur_root.left and not cur_root.right:
                    rep.append(cur_path)
                else:
                    if cur_root.left:
                        root_list.append(cur_root.left)
                        root_parth.append(cur_path+'->'+str(cur_root.left.val))
                    if cur_root.right:
                        root_list.append(cur_root.right)
                        root_parth.append(cur_path+'->'+str(cur_root.right.val))
        return rep
