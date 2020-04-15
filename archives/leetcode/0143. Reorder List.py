'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:            
            node=ListNode(0)
            node.next=head
            pfast=node
            pslow=node
            while pfast.next and pfast.next.next:
                pfast=pfast.next.next
                pslow=pslow.next
            if pfast:
                pslow=pslow.next
            
            pseonde=self.reverse(pslow.next)
            pslow.next=None
            pfirst=head
            while pseonde:
                cur=pseonde
                pseonde=pseonde.next
                cur.next=pfirst.next
                pfirst.next=cur
                pfirst=pfirst.next.next
            
    def reverse(self,head):
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
