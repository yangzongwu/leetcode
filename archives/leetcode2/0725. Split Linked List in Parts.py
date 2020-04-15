# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        p=root
        cnt=0
        while p:
            cnt+=1
            p=p.next
        
        m=cnt//k
        n=cnt%k
        #first n , m+1 ;then should be m
        rep=[]
        for _ in range(n):
            cur=[]
            for _ in range(m+1):
                cur.append(root.val)
                root=root.next
            rep.append(cur)
        print(rep,cnt,n,m)
        for _ in range(k-n):
            cur=[]
            for _ in range(m):
                cur.append(root.val)
                root=root.next
            rep.append(cur)
        return rep
