"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        root_list=[root]
        cnt=0
        while root_list:
            cnt+=1
            cur_root_count=len(root_list)
            for i in range(cur_root_count):
                cur_root=root_list.pop(0)
                for child in cur_root.children:
                    root_list.append(child)
        return cnt
