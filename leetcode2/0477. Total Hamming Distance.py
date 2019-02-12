########################Time Limit Exceeded##########################################
class Solution:
    def totalHammingDistance(self, nums: 'List[int]') -> 'int':
        rep=0
        for k1 in range(len(nums)):
            for k2 in range(k1+1,len(nums)):
                rep+=self.calHamminDis(nums[k1]^nums[k2])
        return rep
    
    def calHamminDis(self,num):
        rep=0
        while num!=0:
            rep+=num&1
            num=num>>1
        return rep
##################################################################
class Solution:
    def totalHammingDistance(self, nums: 'List[int]') -> 'int':
        rep=0
        for _ in range(32):
            res1,res0=0,0
            k=0
            while k<len(nums):
                if nums[k]&1==1:
                    res1+=1
                else:
                    res0+=1
                nums[k]=nums[k]>>1
                k+=1
            rep+=res1*res0
        return rep
