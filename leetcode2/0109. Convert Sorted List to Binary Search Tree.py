# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        node=ListNode(0)
        node.next=head
        pslow,pfast=node,node
        while pfast and pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
        pright=pslow.next
        pslow.next=None
        pleft=head
        
        root=TreeNode(pright.val)
        root.left=self.sortedListToBST(pleft)
        root.right=self.sortedListToBST(pright.next)
        
        return root
        
