# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G=set(G)
        cnt=0
        flag=0
        while head:
            if head.val not in G:
                if flag==1:
                    cnt+=1
                flag=0
            else:
                flag=1
            head=head.next
        cnt+=flag
        return cnt
