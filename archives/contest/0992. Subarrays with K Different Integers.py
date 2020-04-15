######################Time Limit Exceeded###############################################
class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        rep=0
        kk=0
        while kk<len(A)-K+1:
            cur=set()
            j=0
            tmp=K
            while kk+j<len(A) and tmp>0:
                if A[kk+j] not in cur:
                    cur.add(A[kk+j])
                    tmp-=1
                j+=1
                
            if kk+j==len(A):
                if tmp==0:
                    rep+=1
                kk+=1
                continue
                
            
            rep+=1
            i=0
            while kk+j+i<len(A) and A[kk+j+i] in cur:
                rep+=1
                i+=1
            kk+=1
        return rep
        
        
        
