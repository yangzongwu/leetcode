'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child 
pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more 
children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of 
the first level of the list.

Example:
Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
 

Explanation for the above example:
Given the following multilevel doubly linked list:

We should return the following flattened doubly linked list:

'''
##Time Limit Exceeded
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head or not head.next:
            return head
        head_cur=self.listTransfertoArray(head)
        #head_cur=[1,2,3,7,8,11,12,9,10,4,5,6]
        node=Node(head_cur[0],None,None,None)
        cur_node=node
        for val in head_cur[1:]:
            newnode=Node(val,None,None,None)
            cur_node.next=newnode
            newnode.prev=cur_node
            cur_node=cur_node.next
        return node
    
    def listTransfertoArray(self,head):
        head_stack=[head]
        head_cur=[]
        while head_stack:
            curhead=head_stack.pop()
            while curhead:
                head_cur.append(curhead.val)
                if not curhead.child:
                    curhead=curhead.next
                else:
                    head_stack.append(curhead.next)
                    curhead=curhead.child
        return head_cur
 #######
 """
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur=head
        if not head:
            return head
        if not head.next and not head.child:
            return head
        if head.next and not head.child:
            cur.next=self.flatten(cur.next)
        if head.child and not head.next:
            pchild=cur.child
            cur.next=self.flatten(pchild)
            cur.child=None
            pchild.prev=cur
        if head.next and head.child:
            pchild=cur.child
            pnext=cur.next
            cur.next=self.flatten(pchild)
            cur.child=None
            pchild.prev=cur
            while cur.next:
                cur=cur.next
            cur.next=self.flatten(pnext)
            pnext.prev=cur
        return head
#################
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur=head
        if not head:
            return head
        if head.child:
            pchild=cur.child
            pnext=cur.next
            cur.next=self.flatten(pchild)
            cur.child=None
            pchild.prev=cur
            while cur.next:
                cur=cur.next
            if pnext:
                cur.next=self.flatten(pnext)
                pnext.prev=cur
        else:
            cur=self.flatten(cur.next)
        return head
