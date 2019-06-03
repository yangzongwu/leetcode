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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        node=ListNode(0)
        node.next=head
        pslow,pfast=node,node
        while pfast.next and pfast.next.next:
            pfast=pfast.next.next
            pslow=pslow.next
        
        treeNode=TreeNode(pslow.next.val)
        treeNode.right=self.sortedListToBST(pslow.next.next)
        pslow.next=None
        treeNode.left=self.sortedListToBST(node.next)
        
        return treeNode
