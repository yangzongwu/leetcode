class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        rep=''
        nums=[x for x in range(1,n+1)]
        while k>0:
            cur=self.cal_n(n-1)
            if k%cur!=0:
                rep+=str(nums[k//cur])
                nums.pop(k//cur)
                k=k%cur
            else:
                rep+=str(nums[k//cur-1])
                nums.pop(k//cur-1)
                k=k%cur
            n-=1
        if nums:
            rep+=''.join(str(x) for x in nums[::-1])
        return rep
                    
        
        
        
    def cal_n(self,n):
        rep=1
        for i in range(1,n+1):
            rep*=i
        return rep
