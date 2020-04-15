class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        rep=0
        for num in nums:
            rep=rep^num
        
        n=0
        while rep&1==0:
            rep=rep>>1
            n+=1
        
        rep=1<<n
        
        c1=0
        c2=0
        for num in nums:
            if num&rep==0:
                c1=c1^num
            else:
                c2=c2^num
        return[c1,c2]
