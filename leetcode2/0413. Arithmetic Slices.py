class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        rep=0
        k=0
        while k<len(A)-1:
            target=A[k+1]-A[k]
            
            j=1
            while k+1+j<len(A) and A[k+1+j]-A[k]==(j+1)*target:
                j+=1
            j-=1 
            
            rep+=self.cal_num(j+2)
            
            k=k+j+1
            
        return rep
    def cal_num(self,n):
        if n<3:return 0
        if n==3:return 1
        
        rep=0
        i=3
        while n>=i:
            rep+=n-i+1
            i+=1
        return rep
