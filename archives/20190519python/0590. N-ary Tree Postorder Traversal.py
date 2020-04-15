"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        rep=[]
        self.sub_postorder(root,rep)
        return rep
    
    def sub_postorder(self,root,rep):
        if root:
            for child in root.children:
                self.sub_postorder(child,rep)
            rep.append(root.val)
        return

#==============================================================
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            cur_root=root_list.pop()
            rep.append(cur_root.val)
            for child in cur_root.children:
                root_list.append(child)
        return rep[::-1]
