"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        rep=[]
        root_list=[root]
        while root_list:
            cur_root=root_list.pop()
            rep.append(cur_root.val)
            for child in cur_root.children[::-1]:
                root_list.append(child)
        return rep
        
        
#================================================================
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        rep=[]
        self.sub_preorder(root,rep)
        return rep
        
    def sub_preorder(self,root,rep):
        if not root:
            return
        rep.append(root.val)
        for child in root.children:
            self.sub_preorder(child,rep)
        return
