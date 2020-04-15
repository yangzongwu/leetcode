"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        if not root:
            return 0
        list_root=[root]
        rep=0
        while list_root:
            rep+=1
            len_list_root=len(list_root)
            for _ in range(len_list_root):
                cur_root=list_root.pop(0)
                for children_root in cur_root.children:
                    list_root.append(children_root)
        return rep
