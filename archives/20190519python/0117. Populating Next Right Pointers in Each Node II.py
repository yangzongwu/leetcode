"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root_stack=[root]
        while root_stack:
            tmp=[]
            for k in range(len(root_stack)-1):
                cur_root=root_stack.pop(0)
                cur_root.next=root_stack[0]
                if cur_root.left:
                    tmp.append(cur_root.left)
                if cur_root.right:
                    tmp.append(cur_root.right)
            cur_root=root_stack.pop(0)
            cur_root.next=None
            if cur_root.left:
                tmp.append(cur_root.left)
            if cur_root.right:
                tmp.append(cur_root.right)
            root_stack=tmp
        return root
