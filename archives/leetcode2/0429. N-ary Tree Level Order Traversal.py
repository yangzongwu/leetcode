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
        list_root=[root]
        rep=[]
        while list_root:
            tmp=[]
            len_list_root=len(list_root)
            for _ in range(len_list_root):
                cur_root=list_root.pop(0)
                tmp.append(cur_root.val)
                for children_root in cur_root.children:
                    list_root.append(children_root)
            rep.append(tmp)
        return rep
