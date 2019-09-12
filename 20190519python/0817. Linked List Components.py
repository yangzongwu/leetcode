# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g_set=set(G)
        cnt=0
        rep=0
        flag=True
        while head:
            if head.val in g_set:
                if flag==True:
                    flag=False
                    cnt+=1
            else:
                if cnt>0:
                    rep+=1
                    flag=True
                    cnt=0
            head=head.next
        if cnt>0:
            rep+=1
        return rep
