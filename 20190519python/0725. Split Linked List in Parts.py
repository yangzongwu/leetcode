# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        len_of_list=self.calLengthOfList(root)
        rep=[]
        if len_of_list<=k:
            while root:
                cur=root.next
                root.next=None
                rep.append(root)
                root=cur
                k-=1
            while k>0:
                rep.append(None)
                k-=1
        else:
            n=len_of_list//k
            fn=len_of_list%k
            self.getFirstNList(n,fn,rep,root,k)
        return rep
    
    def getFirstNList(self,n,fn,rep,root,k):
        if k==0:
            return 
        if fn>0:
            node=ListNode(0)
            node.next=root
            p=node
            cnt=n+1
            while cnt>0:
                cnt-=1
                p=p.next
            cur=p.next
            p.next=None
            rep.append(node.next)
            self.getFirstNList(n,fn-1,rep,cur,k-1)
        else:
            node=ListNode(0)
            node.next=root
            p=node
            cnt=n
            while cnt>0:
                cnt-=1
                p=p.next
            cur=p.next
            p.next=None
            rep.append(node.next)
            self.getFirstNList(n,fn-1,rep,cur,k-1)
    
    def calLengthOfList(self,root):
        k=0
        while root:
            k+=1
            root=root.next
        return k
