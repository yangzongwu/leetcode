class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums=[x for x in range(1,n+1)]
        rep=[]
        while k>0:
            tmp=k//self.cal_n(n)
            k=k%self.cal_n(n)
            if k!=0:
                rep.append(nums[tmp])
                nums.pop(tmp)
                n-=1
            else:
                rep.append(nums[tmp-1])
                nums.pop(tmp-1)
        res=''.join(str(x) for x in rep)+''.join(str(x) for x in nums[::-1])
        return res
        
    def cal_n(self,n):
        rep=1
        for i in range(1,n):
            rep=rep*i
        return rep
