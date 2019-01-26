"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        root_list=[root]
        rep=[]
        while root_list:
            cur_root=root_list.pop()
            rep.append(cur_root.val)
            if cur_root.children:
                for child in cur_root.children[::-1]:
                    root_list.append(child)
        return rep
