# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node=ListNode(0)
        node.next=head
        p=node
        while p.next:
            if p.next.next and p.next.val==p.next.next.val:
                p.next=self.subDeleteDuplicates(p.next,p.next.val,0)
            else:
                p=p.next
        return node.next
    
    def subDeleteDuplicates(self,head,target,flag):
        if not head.next and flag==0:
            return head
        elif not head.next and flag==1:
            return None
        
        if head.next.val!=target and flag==0:
            return head
        elif head.next.val!=target and flag==1:
            return head.next
        else: #head.next.val==target:
            return self.subDeleteDuplicates(head.next,target,1)
            
            
#==================================================================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node=ListNode(0)
        node.next=head
        p=node
        while p.next and p.next.next:
            if p.next.val!=p.next.next.val:
                p=p.next
            else:
                while p.next.next and p.next.val==p.next.next.val:
                    p.next=p.next.next
                p.next=p.next.next
        return node.next
