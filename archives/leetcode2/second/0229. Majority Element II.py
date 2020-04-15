class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if len(nums)==0:
            return []
        if len(nums)<=2:
            return list(set(nums))
        
        a,b=nums[0],nums[1]
        cnta=1
        cntb=1
        
        left=0
        while left<len(nums) and nums[left]==nums[0]:
            left+=1
        if left==len(nums):
            return [nums[0]]
        a,cnta=nums[0],left
        b,cntb=nums[left],1
        
        
        for num in nums[left+1:]:
            if num==a:
                cnta+=1
            elif num==b:
                cntb+=1
            else:
                if cnta==0:
                    cnta=1
                    a=num
                elif cntb==0:
                    cntb=1
                    b=num
                else:
                    cnta-=1
                    cntb-=1
        
        cnta,cntb=0,0
        for num in nums:
            if num==a:cnta+=1
            if num==b:cntb+=1
        
        rep=[]
        if cnta>len(nums)/3:rep.append(a)
        if cntb>len(nums)/3:rep.append(b)
        return rep
