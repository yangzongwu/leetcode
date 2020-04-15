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
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        node=Node(0,None,None,None)
        node.next=head
        p=node
        list_stack=[]
        while list_stack or p.next:
            if not p.next:
                curList=list_stack.pop()
                p.next=curList
                curList.prev=p
            p=p.next
            while p.next or p.child:
                if p.child:
                    if p.next:
                        list_stack.append(p.next)
                    p.child.prev=p
                    p.next=p.child
                    p.child=None
                    p=p.next
                elif not p.child and p.next:
                    p=p.next
        return node.next
