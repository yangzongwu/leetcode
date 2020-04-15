class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        FN,SN,TN=-2**31-1,-2**31-1,-2**31-1
        for num in nums:
            if num>FN:
                FN,SN,TN=num,FN,SN
            elif num >SN and num!=FN:
                SN,TN=num,SN
            elif num>TN and num!=FN and num!=SN:
                TN=num
        if TN>-2**31-1:
            return TN
        return FN
            
