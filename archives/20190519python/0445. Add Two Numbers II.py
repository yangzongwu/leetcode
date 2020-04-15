# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        l1_stack=self.listToStack(l1)
        l2_stack=self.listToStack(l2)
        
        sum_stack=self.sumOfStack(l1_stack,l2_stack)
        
        node=ListNode(0)
        p=node
        for num in sum_stack[::-1]:
            p.next=ListNode(num)
            p=p.next
        return node.next
        
        
    def listToStack(self,l):
        l_stack=[]
        while l:
            l_stack.append(l.val)
            l=l.next
        return l_stack
    
    def sumOfStack(self,l1,l2):
        s_stack=[]
        flag=0
        while l1 and l2:
            cur=l1.pop()+l2.pop()+flag
            if cur>=10:
                flag=1
                s_stack.append(cur-10)
            else:
                flag=0
                s_stack.append(cur)
        while l1:
            cur=l1.pop()+flag
            if cur>=10:
                flag=1
                s_stack.append(cur-10)
            else:
                flag=0
                s_stack.append(cur)
        while l2:
            cur=l2.pop()+flag
            if cur>=10:
                flag=1
                s_stack.append(cur-10)
            else:
                flag=0
                s_stack.append(cur)
        if flag==1:
            s_stack.append(1)
        return s_stack
