class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep=0
        for i in range(32):
            k=0
            tmp=0
            while k<len(nums):
                tmp+=nums[k]&1
                nums[k]=nums[k]>>1
                k+=1
            tmp=(tmp%3)<<(i)
            rep=rep|tmp
        if rep>2**31-1:
            rep-=2**32
        return rep
    
