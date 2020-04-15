class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        res=0
        for i in A:
            if i%2==0:
                res+=i
        
        rep=[]
        for num in queries:
            if A[num[1]]%2==0 and  num[0]%2==0:
                res+=num[0]
                rep.append(res)
            elif A[num[1]]%2!=0 and  num[0]%2!=0:
                res+=A[num[1]]+num[0]
                rep.append(res)
            elif A[num[1]]%2==0 and  num[0]%2!=0:
                res-=A[num[1]]
                rep.append(res)
            else:#A[num[1]]%2!=0 and  num[0]%2==0:
                rep.append(res)
            A[num[1]]+=num[0]
        return rep
    
   
