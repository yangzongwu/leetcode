"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        p=head
        while p:
            node=Node(p.val,None,None)
            node.next=p.next
            p.next=node
            p=p.next.next
            
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            p=p.next.next
            
        oldhead=head
        newhead=head.next
        p_old=oldhead
        p_new=newhead
        while p_new.next:
            p_old.next=p_old.next.next
            p_old=p_old.next
            p_new.next=p_new.next.next
            p_new=p_new.next
        p_old.next=None
        return newhead
