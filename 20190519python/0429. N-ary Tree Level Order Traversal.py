"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            cur_list=[]
            len_root_list=len(root_list)
            for i in range(len_root_list):
                cur_root=root_list.pop(0)
                cur_list.append(cur_root.val)
                for child in cur_root.children:
                    root_list.append(child)
            rep.append(cur_list)
        return rep
