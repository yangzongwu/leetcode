class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        rep=0
        for i in range(32):
            tmp=0
            k=0
            while k<len(nums):
                tmp+=nums[k]&1
                nums[k]=nums[k]>>1
                k+=1
            tmp=tmp%3
            tmp=tmp<<i
            rep+=tmp
        if rep>2**31-1:
            rep=rep-2**32
        return rep
