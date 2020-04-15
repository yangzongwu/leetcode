class Solution:
    def totalHammingDistance(self, nums: 'List[int]') -> 'int':
        rep=0
        for _ in range(32):
            cnt1=0
            cnt0=0
            k=0
            while k<len(nums):
                if nums[k]&1:
                    cnt1+=1
                else:
                    cnt0+=1
                nums[k]=nums[k]>>1
                k+=1
            rep+=cnt1*cnt0
        return rep
            
