class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        tmpsum=0
        i=0
        while i<len(nums) and tmpsum<s:
            tmpsum+=nums[i]
            i+=1
        if tmpsum<s:
            return 0
        
        right=i-1
        left=0
        rep=right-left+1
        tmpsum-=nums[right]
        while right<len(nums):
            tmpsum+=nums[right]
            while tmpsum-nums[left]>=s:
                tmpsum-=nums[left]
                left+=1
            rep=min(rep,right-left+1)
            right+=1
        return rep
