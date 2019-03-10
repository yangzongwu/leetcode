class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        dictAB={}
        k=0
        for k in range(len(A)):
            if A[k]==B[k]:
                if A[k] not in dictAB:
                    dictAB[A[k]]=1
                else:
                    dictAB[A[k]]+=1
            else:
                if A[k] not in dictAB:
                    dictAB[A[k]]=1
                else:
                    dictAB[A[k]]+=1
                if B[k] not in dictAB:
                    dictAB[B[k]]=1
                else:
                    dictAB[B[k]]+=1
        rep=[]
        for key in dictAB:
            if dictAB[key]==len(A):
                rep.append(key)
        
        if not rep:
            return -1
        
        target=rep[0]
        
        cnta=0
        cntb=0
        for s in A:
            if target==s:
                cnta+=1
        for s in B:
            if target==s:
                cntb+=1
        return min(cnta,len(A)-cnta,cntb,len(B)-cntb)
            
