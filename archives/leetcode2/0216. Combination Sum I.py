class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        rep=[]
        
        self.subcombinationSum3(k,n,[],rep)
        
        return rep
    
     def subcombinationSum3(self,k,n,res,rep):
        if k==0:
            return
        if k==1 and 0<n<=9 and n>res[-1]:
            rep.append(res+[n])
            return
        for i in range(1,min(10,n//k+1)):
            if not res or i>res[-1]:
                self.subcombinationSum3(k-1,n-i,res+[i],rep)
            
            
            
