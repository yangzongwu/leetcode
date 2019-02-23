class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        flag=0
        for num in nums:
            flag^=num
        cur=1
        while flag&1!=1:
            flag=flag>>1
            cur=cur<<1
        
        
        a=0
        b=0
        for num in nums:
            if num&cur==0:
                a=a^num
            else:
                b=b^num
      
        return [a,b]
