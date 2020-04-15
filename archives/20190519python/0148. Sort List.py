# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node=ListNode(0)
        node.next=head
        p=node
        pslow,pfast=p,p
        while pfast.next and pfast.next.next:
            pslow=pslow.next
            pfast=pfast.next.next
        cur=pslow.next
        pslow.next=None
        return self.mergeTwoSortList(self.sortList(node.next),self.sortList(cur))
        
    def mergeTwoSortList(self,headA,headB):
        node=ListNode(0)
        p=node
        while headA and headB:
            if headA.val<headB.val:
                p.next=headA
                headA=headA.next
                p=p.next
            else:
                p.next=headB
                headB=headB.next
                p=p.next
        if headA:
            p.next=headA
        if headB:
            p.next=headB
        return node.next
