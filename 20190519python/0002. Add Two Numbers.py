# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag=0
        node=ListNode(0)
        p=node
        while l1 and l2:
            cur=l1.val+l2.val+flag
            if cur>=10:
                p.next=ListNode(cur-10)
                flag=1
            else:
                p.next=ListNode(cur)
                flag=0
            p=p.next
            l1=l1.next
            l2=l2.next
        while l1:
            cur=l1.val+flag
            if cur>=10:
                p.next=ListNode(cur-10)
                flag=1
            else:
                p.next=ListNode(cur)
                flag=0
            p=p.next
            l1=l1.next
        while l2:
            cur=l2.val+flag
            if cur>=10:
                p.next=ListNode(cur-10)
                flag=1
            else:
                p.next=ListNode(cur)
                flag=0
            p=p.next
            l2=l2.next
        if flag:
            p.next=ListNode(1)
        return node.next
