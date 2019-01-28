class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        rep=0
        for num in nums:
            if num==1:
                cnt+=1
            else:
                rep=max(rep,cnt)
                cnt=0
        return max(rep,cnt)
