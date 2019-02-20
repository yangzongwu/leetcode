class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        dictnums={}
        res=0
        cnt=0
        for num in nums:
            res+=num
            if res==k:
                cnt+=1
            if res-k in dictnums:
                cnt+=dictnums[res-k]
            if res not in dictnums:
                dictnums[res]=1
            else:
                dictnums[res]+=1
        return cnt
