'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        node=ListNode(0)
        p=node
        node.next=head

        while m>1:
            p=p.next
            m-=1
            n-=1

        p.next=self.reverse(p.next,n)
        return node.next

    def reverse(self,head,n):
        prev=None
        while n>0:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
            n-=1

        p=prev
        while p.next:
            p=p.next
        p.next=head

        return prev        
