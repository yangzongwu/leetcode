# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # Definition for binary tree with next pointer.
        if not root:
            return 
        root_stack=[root]
        while root_stack:
            len_root_stack=len(root_stack)
            for k in range(len_root_stack):
                cur_root=root_stack.pop(0)
                if k==len_root_stack-1:
                    cur_root.next=None
                else:
                    cur_root.next=root_stack[0]
                if cur_root.left:
                    root_stack.append(cur_root.left)
                if cur_root.right:
                    root_stack.append(cur_root.right)
