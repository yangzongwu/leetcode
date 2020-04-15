class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        cur=0
        for num in A:
            if num%2==0:
                cur+=num
        rep=[]
        for query in queries:
            if query[0]%2==0 and A[query[1]]%2==0:
                cur+=query[0]
            elif query[0]%2!=0 and A[query[1]]%2!=0:
                cur+=query[0]+A[query[1]]
            elif query[0]%2==0 and A[query[1]]%2!=0:
                pass
            elif query[0]%2!=0 and A[query[1]]%2==0:
                cur-=A[query[1]]
            rep.append(cur)
            A[query[1]]+=query[0]
        
        return rep
