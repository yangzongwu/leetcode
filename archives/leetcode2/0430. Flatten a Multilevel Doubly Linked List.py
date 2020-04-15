"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        stack_head=[]
        
        p=head        
        while p.next or p.child:
            if p.child:
                if p.next:
                    stack_head.append(p.next)
                p.child.prev=p
                p.next=p.child
                p.child=None
            p=p.next
            
        while stack_head:
            cur=stack_head.pop()
            cur.prev=p
            p.next=cur
            while p.next or p.child:
                if p.child:
                    if p.next:
                        stack_head.append(p.next)
                    p.child.prev=p
                    p.next=p.child
                    p.child=None
                p=p.next
            
        return head
